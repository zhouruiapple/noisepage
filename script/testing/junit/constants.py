#!/usr/bin/python3
import os
from util.constants import DIR_TESTING

# settings of TestJUnit
JUNIT_TEST_DIR = os.path.join(DIR_TESTING, "junit")
JUNIT_TEST_ERROR_MSG = "Error: failed to complete junit test"
JUNIT_OUTPUT_FILE = "/tmp/junit_log.txt"

JUNIT_TEST_CMD_ALL = "ant test-all"
JUNIT_TEST_CMD_JUNIT = "ant test-unit"
JUNIT_TEST_CMD_TRACE = "ant test-trace"

JUNIT_OPTION_DIR = os.path.join(JUNIT_TEST_DIR, "out")
JUNIT_OPTION_XML = os.path.join(JUNIT_OPTION_DIR, "options.xml")

REPO_TRACE_DIR = os.path.join("junit", "traces")
TESTFILES_PREFIX = ".test"

DEFAULT_PREPARE_THRESHOLD = 5
