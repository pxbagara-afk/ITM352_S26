def determine_progress3(total, spins):
    """Progress function implemented using if/elif (no nested ifs).

    Behaves like previous versions:
    - "Invalid total" when total <= 0
    - "Get going!" when spins == 0
    - "Keep going!" when spins < total/2
    - "Almost there!" when spins < total
    - "Done!" otherwise
    """
    if total <= 0:
        return "Invalid total"
    if spins == 0:
        return "Get going!"
    if spins < total / 2:
        return "Keep going!"
    elif spins < total:
        return "Almost there!"
    else:
        return "Done!"


def test_determine_progress(progress_function):
    assert progress_function(10, 0) == "Get going!", "spins==0 failed"
    assert progress_function(10, 2) == "Keep going!", "below 50% failed"
    assert progress_function(10, 5) == "Almost there!", "50% boundary failed"
    assert progress_function(10, 10) == "Done!", "complete failed"
    return True


if __name__ == "__main__":
    test_determine_progress(determine_progress3)
    print("All determine_progress3 tests passed")
