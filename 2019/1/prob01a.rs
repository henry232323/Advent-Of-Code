use std::fs;

fn main() {
    let mut sum = 0;

    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    let nums = data.split("\n");
    for num in nums {
        sum += fuel(num.parse::<i32>().unwrap());
    }

    println!("{}", sum);
}

fn fuel(m: i32) -> i32 {
    return (m / 3) - 2;
}