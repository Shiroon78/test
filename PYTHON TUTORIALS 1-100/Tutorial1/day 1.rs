fn main() {
    let number = 7;
    
    // Printing a message based on the value of the number
    if number < 5 {
        println!("The number is less than 5");
    } else if number > 10 {
        println!("The number is greater than 10");
    } else {
        println!("The number is between 5 and 10");
    }
    
    // Calling a function to calculate the square of a number
    let result = square(number);
    println!("The square of {} is {}", number, result);
}

// Function to calculate the square of a number
fn square(x: i32) -> i32 {
    x * x
}
