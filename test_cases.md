
# Test Cases for Aegean Tour Itinerary Solver

## Test Case 1:
Input:
6
4
0 by-sea, 2 by-sea, 3 by-sea
0 by-sea, 5 airborne
0 airborne, 5 by-sea
2 airborne

Expected Output:
0 by-sea, 1 by-sea, 2 airborne, 3 by-sea, 4 by-sea, 5 by-sea

---

## Test Case 2:
Input:
2
3
0 by-sea
0 airborne
1 by-sea

Expected Output:
NO ITINERARY

---

## Test Case 3:
Input:
3
2
0 by-sea
1 by-sea, 2 airborne

Expected Output:
0 by-sea, 1 by-sea, 2 by-sea

---

## Test Case 4:
Input:
3
3
0 by-sea
1 by-sea
2 by-sea

Expected Output:
0 by-sea, 1 by-sea, 2 by-sea

---

## Test Case 5:
Input:
2
3
0 by-sea
0 airborne, 1 by-sea
1 airborne

Expected Output:
NO ITINERARY

---

## Test Case 6:
Input:
2
2
0 by-sea
0 airborne

Expected Output:
NO ITINERARY

---

## Test Case 7:
Input:
4
3
0 airborne
1 by-sea, 2 airborne
2 airborne, 3 by-sea

Expected Output:
0 airborne, 1 by-sea, 2 by-sea, 3 by-sea

---

## Test Case 8:
Input:
5
5
0 by-sea
1 by-sea
2 by-sea
3 by-sea
4 by-sea

Expected Output:
0 by-sea, 1 by-sea, 2 by-sea, 3 by-sea, 4 by-sea

---

## Test Case 9:
Input:
4
2
0 by-sea, 2 airborne
1 by-sea, 3 airborne

Expected Output:
0 by-sea, 1 by-sea, 2 by-sea, 3 by-sea

---

## Test Case 10:
Input:
3
3
0 by-sea
1 by-sea
2 by-sea, 2 airborne

Expected Output:
0 by-sea, 1 by-sea, 2 by-sea

---

## Test Case 11:
Input:
4
2
0 airborne, 1 by-sea
2 airborne, 3 by-sea

Expected Output:
0 by-sea, 1 by-sea, 2 by-sea, 3 by-sea

---

## Test Case 12:
Input:
1
2
0 by-sea
0 airborne

Expected Output:
NO ITINERARY

---

## Test Case 13: Customers with Conflicts on Different Hops
Input:
5
4
0 by-sea
1 airborne
2 by-sea
3 airborne, 4 by-sea

Expected Output:
0 by-sea, 1 airborne, 2 by-sea, 3 by-sea, 4 by-sea

---

## Test Case 14:
Input:
3
3
0 by-sea
1 by-sea
2 by-sea

Expected Output:
0 by-sea, 1 by-sea, 2 by-sea

---

## Test Case 15:
Input:
3
2
0 airborne
0 airborne, 2 by-sea

Expected Output:
0 airborne, 1 by-sea, 2 by-sea

---