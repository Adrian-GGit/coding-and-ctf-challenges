use std::io;
use std::io::Read;

fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}

fn main() {
    // let null_byte: u8 = 0x00u8;
    // println!("Null byte: {}", null_byte);
    // print_type_of(&null_byte);
    // let null_byte_chr = null_byte as char;
    // println!("Null byte chr: {}", null_byte_chr);
    // print_type_of(&null_byte_chr);

    println!("Bytecode: ");
    for i in io::stdin().bytes() {
        // print_type_of(i.as_ref().unwrap());
        match i.unwrap() {
            0x00 => println!("REACHED NULLBYTE"),
            x => println!("x: {}", x),
        }
    }
    println!("Finished")
}

// fn main() {
//     println!("Bytecode: ");
//     let mut buffer = String::new();
//     io::stdin().read_line(&mut buffer);
//     println!("input: {}", buffer);
//     for i in buffer.bytes() {
//         println!("i: {}", i);
//     }
// }