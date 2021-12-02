use day2::util;

fn main() {
    let lines = util::read_lines("input.txt").unwrap();
    part1(&lines);
    part2(&lines);
}

fn part1(lines: &Vec<String>) {
    let mut position = 0;
    let mut depth = 0;
    for l in lines {
        if let Some((instruction, value)) = l.split_once(" ") {
            let int_value = value.parse::<i32>().unwrap();
            match instruction {
                "forward" => position += int_value,
                "down" => depth += int_value,
                "up" => depth -= int_value,
                _ => {}
            }
        }

    }
    println!("{}", position * depth);
}

fn part2(lines: &Vec<String>) {
    let mut position = 0;
    let mut depth = 0;
    let mut aim = 0;
    for l in lines {
        if let Some((instruction, value)) = l.split_once(" ") {
            let i_value = value.parse::<i32>().unwrap();
            match instruction {
                "forward" => {
                    position += i_value;
                    depth += aim * i_value
                },
                "down" => aim += i_value,
                "up" => aim -= i_value,
                _ => {}
            }
        }

    }
    println!("{}", position * depth);
}
