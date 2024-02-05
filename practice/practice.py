if __name__=="__main__":

    def bitwiseAnd(N, K):
        # Write your code here
        K_bin =bin(K-1)[2:]
        N_bin = bin(N)[2:]
        complement_exponent = len(K_bin)
        min_complement = K-1
        max_complement = (2**(complement_exponent+1) - 1)
        
        if K % 2 == 0:     
            
            if max_complement <= N :
                max_val1 = max_complement & min_complement
            else:
                complement=''
                if (lenght_dif:=len(N_bin)-len(K_bin)):
                    K_bin='0'*(lenght_dif)+K_bin   
                flag=True
                for i in range(len(N_bin)):
                    if flag is True:
                        if K_bin[i] == '0' and N_bin[i] == '1':
                            complement+='0'
                            flag=False
                        else:
                            complement+=N_bin[i]
                    else:
                        complement+='1'
                print(N_bin, N)
                print(K_bin, K-1)
                print(complement, int(complement,2))
                print("")
                complement=int(complement,2)

                if complement == K-1:
                    complement-=1
                
                max_val1 = max(complement & (K-1), N & (K-1))
                
        else:
            max_val1 = K & (K-1)
        
        return max_val1

assert bitwiseAnd(983, 896) == 894
assert bitwiseAnd(200, 164) == 163
assert bitwiseAnd(178, 104) == 103
assert bitwiseAnd(127, 64) == 63
assert bitwiseAnd(123, 122) == 121