// Project Euler problem #43 - Substring Divisibility
// Finished

public class Pe43 {

   private static boolean[] exclude(boolean[] multiples, int ... choices) {

      boolean[] newMultiples = new boolean[999];
      for (int i = 0; i < 999; i += 1) {
         newMultiples[i] = true;
      }

      for (int i = 0; i < 999; i += 1) {
         for (int choice : choices) {

            if (multiples[i]) {
               newMultiples[i] = true;
            } else {
               newMultiples[i] = false;
            }

            if ((choice == 0) && ((i + 1) % 100) == (i + 1)) {
            	newMultiples[i] = false;
            	break;
            }

            if (((i + 1) % 100) == (i + 1)) {   // double digit num
               if (((int)Math.floor((i + 1) / 10)) == choice) {
                  newMultiples[i] = false;
                  break;
               } else if (((int)((i + 1) % 10)) == choice) {
                  newMultiples[i] = false;
                  break;
               }
            } else {                            // triple digit num
               if ((int)Math.floor((i + 1) / 100) == choice) {
                  newMultiples[i] = false;
                  break;
               } else if ((int)Math.floor(((i + 1) % 100) / 10) == choice) {
                  newMultiples[i] = false;
                  break;
               } else if (((int)((i + 1) % 10)) == choice) {
                  newMultiples[i] = false;
                  break;
               } 
            }
         }
      }
      return newMultiples;
   }

	public static void main(String[] args) {

		boolean[] multiplesOfTwo = new boolean[999];
		boolean[] multiplesOfSeven = new boolean[999];
		boolean[] multiplesOfSeventeen = new boolean[999];

		for (int i = 0; i < 999; i += 1) {
			multiplesOfTwo[i] = false;
			multiplesOfSeven[i] = false;
			multiplesOfSeventeen[i] = false;
		}

		for (int i = 0; i < 999; i += 1) {
			if (i % 2 == 1) {
				multiplesOfTwo[i] = true;
			}
		}

		for (int i = 0; i < 999; i += 1) {
			if (i % 7 == 6) {
				multiplesOfSeven[i] = true;
			}
		}

		for (int i = 0; i < 999; i += 1) {
			if (i % 17 == 16) {
				multiplesOfSeventeen[i] = true;
			}
		}

		// 4,118,000 total 10 digit numbers possible
		int d6;
		for (int i = 0; i < 999; i += 1) {
			if (multiplesOfSeven[i] && ((i + 1) < 10)) {
				d6 = ((i + 1) % 10);
				if ((d6 != 0) && (d6 != 5)) {
					multiplesOfSeven[i] = false;
				}
			} else if (multiplesOfSeven[i] && ((i + 1) < 100)) {
				d6 = ((int)Math.floor((i + 1) / 10));
				if ((d6 != 0) && (d6 != 5)) {
					multiplesOfSeven[i] = false;
				}
			} else if (multiplesOfSeven[i]) {
				d6 = ((int)Math.floor(((i + 1) % 100) / 10));
				if ((d6 != 0) && (d6 != 5)) {
					multiplesOfSeven[i] = false;
				}
			}
		}	

		// 754,000 total 10 digit numbers possible

		for (int i = 12; i < 999; i += 2) {
			if (((i % 100) % 10) == (int)(Math.floor((i % 100) / 10))) {
				multiplesOfTwo[i - 1] = false;
			} else if ((i % 100 == i) && (0 == ((i % 100) % 10))) {
				multiplesOfTwo[i - 1] = false;
			} else if ((i % 100 == i)) {
				continue;
			} else if (((int)(Math.floor(i / 100)) == ((i % 100) % 10) || ((int)(Math.floor(i / 100))) == ((int)(Math.floor((i % 100) / 10))))) {
				multiplesOfTwo[i - 1] = false;
			}
		}

		for (int i = 14; i < 999; i += 7) {
			if (((i % 100) % 10) == ((int)(Math.floor((i % 100) / 10)))) {
				multiplesOfSeven[i - 1] = false;
			} else if ((i % 100 == i) && (0 == ((i % 100) % 10))) {
				multiplesOfSeven[i - 1] = false;
			} else if ((i % 100 == i)) {
				continue;
			} else if (((int)(Math.floor(i / 100)) == ((i % 100) % 10) || ((int)(Math.floor(i / 100))) == ((int)(Math.floor((i % 100) / 10))))) {
				multiplesOfSeven[i - 1] = false;
			}
		}
		
		for (int i = 17; i < 999; i += 17) {
			if (((i % 100) % 10) == ((int)(Math.floor((i % 100) / 10)))) {
				multiplesOfSeventeen[i - 1] = false;
			} else if ((i % 100 == i) && (0 == ((i % 100) % 10))) {
				multiplesOfSeventeen[i - 1] = false;
			} else if ((i % 100 == i)) {
				continue;
			} else if (((int)(Math.floor(i / 100)) == ((i % 100) % 10) || ((int)(Math.floor(i / 100))) == ((int)(Math.floor((i % 100) / 10))))) {
				multiplesOfSeventeen[i - 1] = false;
			}
		}

		// 417,560 total 10 digit numbers possible
		String pandigitalString = "";
		long pandigital;
		long result = 0;

		boolean[] multiplesOfTwoForK = new boolean[999];
		boolean[] multiplesOfSevenForK = new boolean[999];
		boolean[] multiplesOfSeventeenForK = new boolean[999];	

		boolean[] multiplesOfTwoForJ = new boolean[999];
		boolean[] multiplesOfSevenForJ = new boolean[999];	

		boolean[] multiplesOfTwoForI = new boolean[999];
		int lastAllocateSize = 100;
		long[] pandigitalArray = new long[lastAllocateSize];

		pandigitalArray[0] = 1;
		for (int i = 1; i < lastAllocateSize; ++i) {
			pandigitalArray[i] = 0;
		}

		// bias the search to exclude choosen value
		for (int choose = 1; choose < 10; ++choose) {

			multiplesOfTwoForK = exclude(multiplesOfTwo, choose);
			multiplesOfSevenForK = exclude(multiplesOfSeven, choose);
			multiplesOfSeventeenForK = exclude(multiplesOfSeventeen, choose);

			for (int k = 16; k < 999; k += 17) {	// 17

				if (multiplesOfSeventeenForK[k] == false) {
					continue;
				} else if (multiplesOfSeventeenForK[k] && (k < 99)) {
					multiplesOfSevenForJ = exclude(multiplesOfSevenForK, 0, ((int)Math.floor((k + 1) / 10)), ((int)((k + 1) % 10)));
					multiplesOfTwoForJ = exclude(multiplesOfTwoForK, 0, ((int)Math.floor((k + 1) / 10)), ((int)((k + 1) % 10)));
				} else if (multiplesOfSeventeenForK[k] && (k < 999)) {
					multiplesOfSevenForJ = exclude(multiplesOfSevenForK, ((int)Math.floor((k + 1) / 100)), ((int)Math.floor(((k + 1) % 100) / 10)), ((int)Math.floor(((k + 1) % 100) % 10)));
					multiplesOfTwoForJ = exclude(multiplesOfTwoForK, ((int)Math.floor((k + 1) / 100)), ((int)Math.floor(((k + 1) % 100) / 10)), ((int)Math.floor(((k + 1) % 100) % 10)));
				}

				for (int j = 13; j < 999; j += 7) {	// 14
					
					if (multiplesOfSevenForJ[j] == false) {
						continue;
					} else if (multiplesOfSevenForJ[j] && (j < 99)) {
						multiplesOfTwoForI = exclude(multiplesOfTwoForJ, 0, ((int)Math.floor((j + 1) / 10)), ((int)(j + 1) % 10));
					} else if (multiplesOfSevenForJ[j] && (j < 999)) {
						multiplesOfTwoForI = exclude(multiplesOfTwoForJ, ((int)Math.floor((j + 1) / 100)), ((int)Math.floor(((j + 1) % 100) / 10)), ((int)Math.floor(((j + 1) % 100) % 10)));
					}

					for (int i = 11; i < 999; i += 2) {	// 12

						if (multiplesOfTwoForI[i]) {
							if (i < 99) {
								pandigitalString = choose + "0" + (i + 1) + "" + (j + 1) + "" + (k + 1);
							} else if (j < 99) {
								pandigitalString = choose + "" + (i + 1) + "0" + (j + 1) + "" + (k + 1);
							} else if (k < 99) {
								pandigitalString = choose + "" + (i + 1) + "" + (j + 1) + "0" + (k + 1);
							} else {
								pandigitalString = choose + "" + (i + 1) + "" + (j + 1) + "" + (k + 1);
							}		

							pandigital = Long.parseLong(pandigitalString);

							if ((Long.parseLong(pandigitalString.substring(2, 5)) % 3 == 0) && (Long.parseLong(pandigitalString.substring(3, 6)) % 5 == 0)
							&& (Long.parseLong(pandigitalString.substring(5, 8)) % 11 == 0) && (Long.parseLong(pandigitalString.substring(6, 9)) % 13 == 0)) {
								System.out.println(pandigital);
								result += pandigital;
							}
						}
					}
				}
			}
		}
		System.out.println(result);
	}
}