toolchain(
    name = "toolchain_for_x86_64-unknown-freebsd",
    exec_compatible_with = ["@platforms//cpu:x86_64", "@platforms//os:freebsd"],
    target_compatible_with = ["@platforms//cpu:x86_64", "@platforms//os:freebsd"],
    toolchain = "@rust_freebsd_x86_64//:toolchain_for_x86_64-unknown-freebsd_impl",
    toolchain_type = "@io_bazel_rules_rust//rust:toolchain",
)

toolchain(
    name = "toolchain_for_wasm32-unknown-unknown",
    exec_compatible_with = ["@platforms//cpu:x86_64", "@platforms//os:freebsd"],
    target_compatible_with = ["@io_bazel_rules_rust//rust/platform:wasm32"],
    toolchain = "@rust_freebsd_x86_64//:toolchain_for_wasm32-unknown-unknown_impl",
    toolchain_type = "@io_bazel_rules_rust//rust:toolchain",
)
