// "I know a secret x that is NOT equal to your public y."
fn main(x: Field, y: pub Field) {
    assert(x != y);
}

#[test]
fn different_values_pass() {
    main(1, 2);
}

#[test(should_fail)]
fn equal_values_fail() {
    main(7, 7);
}
