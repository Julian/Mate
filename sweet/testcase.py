from unittest import TestCase as PyUnitTestCase


class MatcherSupportMixin(object):
    def assertThat(self, result, matcher):
        """
        Assert that the result matches via the given matcher.

        :argument result: the result to try and match
        :argument matcher: the Matcher to use

        """

        mismatch = matcher.match(result)
        if mismatch is not None:
            self.fail(mismatch.describe())


class TestCase(MatcherSupportMixin, PyUnitTestCase):
    pass
