// Project Euler problem 17 - Number Letter Counts
// Finished

public class Pe17 {
	public static void main(String args[]) {

		String[] numbersInEnglishOnes = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
		String[] special = {"eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
		String[] numbersInEnglishTens = {"ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninty"};
		String[] numbersInEnglishRest = {"hundred", "thousand"};
	
		int result = 0;

		int firstDigit = 0;
		int secondDigit = 0;
		int thirdDigit = 0;

		boolean testForSpecials;
		for (int i = 1; i < 1001; ++i) {

			firstDigit = 0;
			secondDigit = 0;
			thirdDigit = 0;

			if ((i % 10) != 0) {
				thirdDigit = ((int)(i % 10));
			}
			if (i > 9) { 
				secondDigit = ((int)(Math.floor((i % 100) / 10)));
			}
			if (i > 99) {
				firstDigit = ((int)(Math.floor(i / 100)));
			}
			testForSpecials = ((secondDigit == 1) && ((i % 10) != 0) ? true : false);
			System.out.print(i + ": ");
			System.out.print(" " + secondDigit + " " + thirdDigit + " ");
			if (i == 1000) {
				System.out.println(numbersInEnglishOnes[0] + numbersInEnglishRest[1]);
				result += numbersInEnglishOnes[0].length() + numbersInEnglishRest[1].length();
			} else if (i < 10) {
				System.out.println(numbersInEnglishOnes[i - 1]);
				result += numbersInEnglishOnes[thirdDigit - 1].length();
			} else if (testForSpecials) {
				if (i > 99) {
					System.out.println(numbersInEnglishOnes[firstDigit - 1] + numbersInEnglishRest[0] + "and" + special[thirdDigit - 1]);
					result += 3 + numbersInEnglishOnes[firstDigit - 1].length() + numbersInEnglishRest[0].length() + special[thirdDigit - 1].length();
				} else {
					System.out.println(special[thirdDigit - 1]);
					result += special[thirdDigit - 1].length();
				} 
			} else if ((i % 100) == i) {		// double digit number
				if ((i % 10) == 0) {
					result += numbersInEnglishTens[secondDigit - 1].length();
					System.out.println(numbersInEnglishTens[secondDigit - 1]);
				} else {
					result += numbersInEnglishTens[secondDigit - 1].length() + numbersInEnglishOnes[thirdDigit - 1].length();
					System.out.println(numbersInEnglishTens[secondDigit - 1] + numbersInEnglishOnes[thirdDigit - 1]);				
				}
			} else if (((i % 100) == 0) && thirdDigit != 0) {
				result += numbersInEnglishOnes[thirdDigit - 1].length() + numbersInEnglishRest[0].length();
				System.out.println(numbersInEnglishOnes[thirdDigit - 1] + numbersInEnglishRest[0]);
			} else if ((i % 1000) == i) {		// triple digit number
				if ((thirdDigit == 0) && (secondDigit == 0)) {
					result += numbersInEnglishOnes[firstDigit - 1].length() + numbersInEnglishRest[0].length();
					System.out.println(numbersInEnglishOnes[firstDigit - 1] + numbersInEnglishRest[0]);
				} else if (thirdDigit == 0) {
					result += numbersInEnglishOnes[firstDigit - 1].length() + numbersInEnglishRest[0].length() + 3 + numbersInEnglishTens[secondDigit - 1].length();
					System.out.println(numbersInEnglishOnes[firstDigit - 1] + numbersInEnglishRest[0] + "and" + numbersInEnglishTens[secondDigit - 1]);
				} else if (secondDigit == 0) {
					result += numbersInEnglishOnes[firstDigit - 1].length() + numbersInEnglishRest[0].length() + 3 + numbersInEnglishOnes[thirdDigit - 1].length();
					System.out.println(numbersInEnglishOnes[firstDigit - 1] + numbersInEnglishRest[0] + "and" + numbersInEnglishOnes[thirdDigit - 1]);
				} else {
					result += numbersInEnglishOnes[firstDigit - 1].length() + numbersInEnglishRest[0].length() + 3 + numbersInEnglishTens[secondDigit - 1].length() + numbersInEnglishOnes[thirdDigit - 1].length();
					System.out.println(numbersInEnglishOnes[firstDigit - 1] + numbersInEnglishRest[0] + "and" + numbersInEnglishTens[secondDigit - 1] + numbersInEnglishOnes[thirdDigit - 1]);
				}
			}
		}
		System.out.println(result);
	}
}