
def determine_progress1(total, spins):
   if total <= 0:
      return "Invalid total"
   if spins == 0:
      return "Get going!"
   if spins < total / 2:
      return "Keep going!"
   if spins < total:
      return "Almost there!"
   return "Done!"


def test_determine_progress(progress_function):
   # Four simple asserts covering each main outcome
   assert progress_function(10, 0) == "Get going!", "spins==0 failed"
   assert progress_function(10, 2) == "Keep going!", "below 50% failed"
   assert progress_function(10, 5) == "Almost there!", "50% boundary failed"
   assert progress_function(10, 10) == "Done!", "complete failed"
   return True


if __name__ == "__main__":
   test_determine_progress(determine_progress1)
   print("All determine_progress1 tests passed")

   # determine_progress2: same behavior but implemented without elif/else and no nested ifs
   def determine_progress2(total, spins):
      if total <= 0:
         return "Invalid total"
      if spins == 0:
         return "Get going!"
      if spins < total / 2:
         return "Keep going!"
      if spins < total:
         return "Almost there!"
      return "Done!"

   # Run the same test suite against determine_progress2
   test_determine_progress(determine_progress2)
   print("All determine_progress2 tests passed")
