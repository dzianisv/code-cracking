mod external;

fn main() {
    println!("Hello, world!");
    unsafe {
        external::do_it();
    }
}
