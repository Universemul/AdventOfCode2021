use day1::util;

fn main() {
    let lines = util::read_ints("input.txt");
    part1(&lines);
    part2(&lines);
}

fn part1(lines: &Vec<i32>) {
    let mut increased = 0;
    for pos in 1..lines.len() {
        if lines[pos - 1] < lines[pos] {
            increased += 1;
        }
    }
    println!("{}", increased);
}


fn part2(lines: &Vec<i32>) {
    let mut increased = 0;
    for pos in 3..lines.len() {
        let a:i32 = lines[pos-3..pos].iter().sum();
        let b:i32 = lines[pos-2..=pos].iter().sum();
        if a < b {
            increased += 1;
        }
    }
    println!("{}", increased);
}
