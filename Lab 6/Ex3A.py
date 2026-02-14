
if __name__ == "__main__":
   test_determine_progress(determine_progress1)
   print("All determine_progress1 tests passed")

   # determine_progress2: same behavior, implemented without nested ifs, no elif/else
   def determine_progress2(total, spins):
      # guard clause for invalid total
      if total <= 0:
         return "Invalid total"

      # guard clause for zero spins
      if spins == 0:
         return "Get going!"

      # compute flags and return using sequential guards (no nesting, no elif/else)
      less_than_half = spins < total / 2
      less_than_total = spins < total

      if less_than_half:
         return "Keep going!"
      if less_than_total:
         return "Almost there!"
      return "Done!"

   # Run same simple tests on determine_progress2
   test_determine_progress(determine_progress2)
   print("All determine_progress2 tests passed")
