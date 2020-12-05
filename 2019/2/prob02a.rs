use std::fs;

fn main() {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    let snums: Vec<&str> = data.split(",").collect();
    let mut tnums: Vec<usize> = snums.into_iter().map(|x| x.trim().parse::<usize>().unwrap()).collect();
    tnums[1] = 12;
    tnums[2] = 2;

    let mut i = 0;
    while i < tnums.len() {
        let nums = &mut tnums;
        if nums[i] == 99 {
            break;
        }
        let p3 = nums[i + 3];
        let p2 = nums[i + 2];
        let p1 = nums[i + 1];

        if nums[i] == 1 {
            nums[p3] = nums[p2] + nums[p1];
        } else if nums[i] == 2 {
            nums[p3] = nums[p2] * nums[p1];
        } else {
            break;
        }
        i += 4;
    }

    println!("{}", tnums[0]);
}
