
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

OPENSSL_DISABLED_EXTENSIONS = [
            "envoy.tls.key_providers.cryptomb",
            "envoy.tls.key_providers.qat",
            "envoy.quic.deterministic_connection_id_generator",
            "envoy.quic.crypto_stream.server.quiche",
            "envoy.quic.proof_source.filter_chain",
        ]

def load_envoy():
    http_archive(
        name = "envoy",
        sha256 = "fe1440efd040c6b8121735b8b0f1e15cd2b836c4a8f9962027cf89fd07157f46",
        strip_prefix = "envoy-openssl-20e5efc5008fca67672627e28bf689a452dfe013",
        url = "https://github.com/envoyproxy/envoy-openssl/archive/20e5efc5008fca67672627e28bf689a452dfe013.tar.gz",
        patch_args = ["-p1"],
        patches = [
            "@io_istio_proxy//ossm/patches:use-cmake-from-host.patch",
            ],
    )
