# Sky Fragment Eruption Map Generator

## Project Description

This project is a fragment eruption time and map generator for the game *Sky: Children of the Light*. The user inputs a date, and the program outputs the corresponding fragment eruption time slot, map name, and generates a table displaying the fragment eruption times for different maps on various days of the week.

### Features:
1. **Fragment Eruption Check**: Based on the input date, the program determines if it is `sharp_before` or `sharp_after`.
2. **Map Name Generation**: Based on the day of the month, the program generates the corresponding map name. The map names follow a repeating cycle:
   - Day 1: *The Land of the Golden Wasteland* (暮土)
   - Day 2: *Forbidden Vault* (禁阁)
   - Day 3: *The Clouded Forest* (云野)
   - Day 4: *The Rainforest* (雨林)
   - Day 5: *The Valley of Dawn* (霞谷)
   - From Day 6 onwards, the cycle repeats.
3. **Time Slot Generation**: The program generates a specific time slot based on the weekday of the input date.
4. **Plain Text Table Output**: The program outputs a plain text table displaying the fragment eruption times for various maps on different weekdays.

## Project Structure

