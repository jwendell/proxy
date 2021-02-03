toolchain(
    name = "toolchain_for_x86_64-apple-darwin",
    exec_compatible_with = ["@platforms//cpu:x86_64", "@platforms//os:osx"],
    target_compatible_with = ["@platforms//cpu:x86_64", "@platforms//os:osx"],
    toolchain = "@rust_darwin_x86_64//:toolchain_for_x86_64-apple-darwin_impl",
    toolchain_type = "@io_bazel_rules_rust//rust:toolchain",
)

toolchain(
    name = "toolchain_for_wasm32-unknown-unknown",
    exec_compatible_with = ["@platforms//cpu:x86_64", "@platforms//os:osx"],
    target_compatible_with = ["@io_bazel_rules_rust//rust/platform:wasm32"],
    toolchain = "@rust_darwin_x86_64//:toolchain_for_wasm32-unknown-unknown_impl",
    toolchain_type = "@io_bazel_rules_rust//rust:toolchain",
)
