def Longest_Palindrome(string S, string S') {
        # // S' == S with a bogus character (eg. '|') inserted 
        # // between each character (including outer boundaries)

        # // The radius of the longest palindrome centered on each place in S'
        # // note: length(S') = length(PalindromeRadii) = 2 × length(S) + 1

        PalindromeRadii = [0,...,0]
        Center = 0
        Radius = 0
        
        while Center < length(S') {
	    # // At the start of the loop, Radius is already set to a lower-bound
	    # // for the longest radius. In the first iteration, Radius is 0, but
	    # // it can be higher on later iterations.
            
	    # // Determine the longest palindrome starting at Center-Radius and
	    # // going to Center+Radius
        while Center < 

            while Center < length(S') and 
	          Center+(Radius+1) < length(S') and 
		  S'[Center-(Radius+1)] = S'[Center+(Radius+1)] {
                Radius = Radius+1
            }             
         
            // Save the radius of the longest palindrome in the array
            PalindromeRadii[Center] = Radius
            
            // Below, Center is incremented.
            // If any precomputed values can be reused, they are.
            // Also, Radius may be set to a value greater than 0
            
            OldCenter = Center
            OldRadius = Radius
            Center = Center+1

	    // Radius' default value will be 0, if we reach the end of the
	    // following loop. 
            Radius = 0 

            while Center <= OldCenter + OldRadius {

		// Because Center lies inside the old palindrome and every
		// character inside a palindrome has a "mirrored" character
		// reflected across its center, we can use the data that was
		// precomputed for the Center's mirrored point. 

                MirroredCenter = OldCenter - (Center - OldCenter)
                MaxMirroredRadius = OldCenter + OldRadius - Center

                if PalindromeRadii[MirroredCenter] < MaxMirroredRadius {

		    // The palindrome centered at MirroredCenter is entirely
		    // contained in the palindrome centered at OldCenter So,
		    // MirroredCenter and Center have the same sized palindrome

                    PalindromeRadii[Center] = PalindromeRadii[MirroredCenter]
                    Center = Center+1
                } else if PalindromeRadii[MirroredCenter] > MaxMirroredRadius {
                
		    // The palindrome at MirroredCenter extends beyond the
		    // palindrome at OldCenter The palindrome at Center must
		    // end at the edge of the OldCenter palindrome Otherwise,
		    // the palindrome at OldCenter would be bigger

                    PalindromeRadii[Center] = MaxMirroredRadius
                    Center = Center+1
                } else { // PalindromeRadii[MirroredCenter] = MaxMirroredRadius

		    // Since the palindrome at MirroredCenter ends exactly at
		    // the edge of the palindrome centered at OldCenter, the
		    // palindrome at Center might be bigger Set Radius to the
		    // minimum size of the palindrome at Center so it doesn't
		    // recheck unnecessarily 

                    Radius = MaxMirroredRadius
                    break
                }   
            }      
        }

	// A palindrome's size is equal to its radius * 2. However, since our
	// variable Radius considers our bogus characters to the side of the
	// center, the size of its corresponding palindrome is actually 2 *
	// (Radius / 2), which means a palindrome's size is equal to its
	// corresponding Radius value in PalindromeRadii

        longest_palindrome_in_S = max(PalindromeRadii)
        return longest_palindrome_in_S
    }



sol = Solution()