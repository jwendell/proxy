toolchain(
    name = "toolchain_for_x86_64-pc-windows-msvc",
    exec_compatible_with = ["@platforms//cpu:x86_64", "@platforms//os:windows"],
    target_compatible_with = ["@platforms//cpu:x86_64", "@platforms//os:windows"],
    toolchain = "@rust_windows_x86_64//:toolchain_for_x86_64-pc-windows-msvc_impl",
    toolchain_type = "@io_bazel_rules_rust//rust:toolchain",
)

toolchain(
    name = "toolchain_for_wasm32-unknown-unknown",
    exec_compatible_with = ["@platforms//cpu:x86_64", "@platforms//os:windows"],
    target_compatible_with = ["@io_bazel_rules_rust//rust/platform:wasm32"],
    toolchain = "@rust_windows_x86_64//:toolchain_for_wasm32-unknown-unknown_impl",
    toolchain_type = "@io_bazel_rules_rust//rust:toolchain",
)
