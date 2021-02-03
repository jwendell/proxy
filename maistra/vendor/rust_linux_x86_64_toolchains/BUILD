toolchain(
    name = "toolchain_for_x86_64-unknown-linux-gnu",
    exec_compatible_with = ["@platforms//cpu:x86_64", "@platforms//os:linux"],
    target_compatible_with = ["@platforms//cpu:x86_64", "@platforms//os:linux"],
    toolchain = "@rust_linux_x86_64//:toolchain_for_x86_64-unknown-linux-gnu_impl",
    toolchain_type = "@io_bazel_rules_rust//rust:toolchain",
)

toolchain(
    name = "toolchain_for_wasm32-unknown-unknown",
    exec_compatible_with = ["@platforms//cpu:x86_64", "@platforms//os:linux"],
    target_compatible_with = ["@io_bazel_rules_rust//rust/platform:wasm32"],
    toolchain = "@rust_linux_x86_64//:toolchain_for_wasm32-unknown-unknown_impl",
    toolchain_type = "@io_bazel_rules_rust//rust:toolchain",
)
