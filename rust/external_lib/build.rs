extern crate cc;

fn main() {
    println!("cargo:rustc-link-lib=static=external");

    cc::Build::new()
        .cpp(true)
        .file("src/external.cpp")
        .compile("external");
}