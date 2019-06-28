import mock
from django.core.management import CommandError
from django.test import TestCase

from course_discovery.apps.course_metadata.choices import CourseRunStatus
from course_discovery.apps.course_metadata.exceptions import RedirectCreateError
from course_discovery.apps.course_metadata.management.commands.update_marketing_redirects import Command
from course_discovery.apps.course_metadata.tests.factories import CourseFactory, CourseRunFactory


@mock.patch('course_discovery.apps.course_metadata.models.Course.update_marketing_redirects')
class PublishLiveCourseRunsTests(TestCase):
    def handle(self):
        Command().handle()

    def test_filtering_and_grouping(self, mock_redirect):
        course1 = CourseFactory()
        course2 = CourseFactory()
        course3 = CourseFactory()
        run1 = CourseRunFactory(status=CourseRunStatus.Published, course=course2)  # all intentionally out of order
        _run2 = CourseRunFactory(status=CourseRunStatus.Unpublished, course=course2)
        _run3 = CourseRunFactory(status=CourseRunStatus.Unpublished, course=course3)
        run4 = CourseRunFactory(status=CourseRunStatus.Published, course=course1)
        run5 = CourseRunFactory(status=CourseRunStatus.Published, course=course2)

        self.handle()

        self.assertNumQueries(1)
        self.assertEqual(mock_redirect.call_count, 2)
        self.assertEqual(mock_redirect.call_args_list[0], mock.call(published_runs={run4}))
        self.assertEqual(mock_redirect.call_args_list[1], mock.call(published_runs={run1, run5}))

    def test_exception_does_not_stop_command(self, mock_redirect):
        CourseRunFactory(status=CourseRunStatus.Published)
        CourseRunFactory(status=CourseRunStatus.Published)

        mock_redirect.side_effect = [RedirectCreateError, None]
        with self.assertRaises(CommandError):
            self.handle()

        self.assertEqual(mock_redirect.call_count, 2)