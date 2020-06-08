# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
################################################################################
#
workspace(name = "io_istio_proxy")

# http_archive is not a native function since bazel 0.19
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load(
    "//:repositories.bzl",
    "docker_dependencies",
    "googletest_repositories",
    "mixerapi_dependencies",
)

googletest_repositories()

mixerapi_dependencies()

new_local_repository(
    name = "openssl",
    path = "/usr/lib64/",
    build_file = "openssl.BUILD"
)

# CURL
new_local_repository(
    name = "maistra_curl_headers",
    path = "/usr/include/curl/",
    build_file_content = """
cc_library(
    name = "headers",
    hdrs = glob(["**/*.h"]),
    visibility = ["//visibility:public"],
)
"""
)
new_local_repository(
    name = "com_github_curl",
    path = "/usr/lib64/",
    build_file_content = """
cc_library(
    name = "curl",
    srcs = ["libcurl.so"],
    deps = ["@maistra_curl_headers//:headers"],
    copts = ["-Iexternal/maistra_curl_headers"],
    visibility = ["//visibility:public"],
)
cc_library(
    name = "all",
    srcs = ["libcurl.so"],
    deps = ["@maistra_curl_headers//:headers"],
    copts = ["-Iexternal/maistra_curl_headers"],
    visibility = ["//visibility:public"],
)
"""
)
bind(
    name = "curl",
    actual = "@com_github_curl//:curl",
)

# 1. Determine SHA256 `wget https://github.com/maistra/envoy/archive/$COMMIT.tar.gz && sha256sum $COMMIT.tar.gz`
# 2. Update .bazelrc and .bazelversion files.
#
# envoy commit date: 06/01/2020
ENVOY_SHA = "34f9a3ab9a849cc2f1b9603626af64409a74d91f"

ENVOY_SHA256 = "4288371b789ceb378433f047fbe76545c035b719faf68339ba8a029a09d5a836"

# To override with local envoy, just pass `--override_repository=envoy=/PATH/TO/ENVOY` to Bazel or
# persist the option in `user.bazelrc`.
http_archive(
    name = "envoy",
    sha256 = ENVOY_SHA256,
    strip_prefix = "envoy-" + ENVOY_SHA,
    url = "https://github.com/maistra/envoy/archive/" + ENVOY_SHA + ".tar.gz",
)

load("@envoy//bazel:api_binding.bzl", "envoy_api_binding")

envoy_api_binding()

load("@envoy//bazel:api_repositories.bzl", "envoy_api_dependencies")

envoy_api_dependencies()

load("@envoy//bazel:repositories.bzl", "envoy_dependencies")

envoy_dependencies()

load("@envoy//bazel:dependency_imports.bzl", "envoy_dependency_imports")

envoy_dependency_imports()

# Docker dependencies

docker_dependencies()

load(
    "@io_bazel_rules_docker//repositories:repositories.bzl",
    container_repositories = "repositories",
)

container_repositories()

load("@io_bazel_rules_docker//repositories:deps.bzl", container_deps = "deps")

container_deps()

load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_pull",
)

container_pull(
    name = "distroless_cc",
    # Latest as of 10/21/2019. To update, remove this line, re-build, and copy the suggested digest.
    digest = "sha256:86f16733f25964c40dcd34edf14339ddbb2287af2f7c9dfad88f0366723c00d7",
    registry = "gcr.io",
    repository = "distroless/cc",
)

container_pull(
    name = "bionic",
    # Latest as of 10/21/2019. To update, remove this line, re-build, and copy the suggested digest.
    digest = "sha256:3e83eca7870ee14a03b8026660e71ba761e6919b6982fb920d10254688a363d4",
    registry = "index.docker.io",
    repository = "library/ubuntu",
    tag = "bionic",
)

# End of docker dependencies

### Maistra dependencies
# WEE8
new_local_repository(
    name = "maistra_wee8_headers",
    path = "/usr/include/wasm-api/",
    build_file_content = """
cc_library(
    name = "headers",
    hdrs = glob(["**/*.h"]),
    visibility = ["//visibility:public"],
)
"""
)
new_local_repository(
    name = "maistra_wee8_libs",
    path = "/usr/lib64/",
    build_file_content = """
cc_library(
    name = "wee8",
    srcs = ["libwee8.a"],
    deps = ["@maistra_wee8_headers//:headers"],
    copts = ["-Iexternal/maistra_wee8_headers"],
    visibility = ["//visibility:public"],
)
"""
)
bind(
    name = "wee8",
    actual = "@maistra_wee8_libs//:wee8",
)
