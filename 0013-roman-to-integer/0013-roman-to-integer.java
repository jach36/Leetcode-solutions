class Solution {
    public int romanToInt(String s) {
        return addAll(findException(setVal(s)));
    }
    public int[] setVal(String s){
        int[] sum= new int[s.length()];
        for(int i  = 0; i<s.length(); i++){
            char val=s.charAt(i);
            if (val=='I'){
                sum[i]= 1;
            }else if(val=='V'){
                sum[i]= 5;
            }else if(val=='X'){
                sum[i]=10;
            }else if(val=='L'){
                sum[i]= 50;
            }else if(val=='C'){
                sum[i]=100;
            }else if(val=='D'){
                sum[i] = 500;
            }else if(val=='M'){
                sum[i]=1000;
            }
            
        }
        return sum;
    }
    public int[] findException(int[] a){
        int [] a2 = new int [a.length]; 
        if(a.length==1){
         return a;   
        }else if(a.length%2==0){
            for(int i= 0; i<a.length; i++){
                if(i==a.length-1){
                    int second = a[a.length-1];
                    int first = a[i-1];
                    int compare= second-first;
                    if(compare==4|| compare ==9 || compare== 40 || compare == 90 || compare == 400 || compare == 900){
                        a2[i]=compare;
                        a[i+1]=0;
                    }
                    else{
                        a2[i]=a[i];
                }
                }
                else{
                    int second = a[i+1];
                    int first = a[i];
                    int compare= second-first;
                    if(compare==4 || compare ==9 || compare== 40 || compare == 90 || compare == 400 || compare == 900){
                        a2[i]=compare;
                        a[i+1]=0;
                        
                    }
                    else{
                        a2[i]=a[i];
                    }
                }
            }
        }
        else{
        for(int i= 0; i<a.length; i++){
            if(i==a.length-1){
                int second = a[a.length-1];
                int first = a[i-1];
                int compare= second-first;
                if(compare==4|| compare ==9 || compare== 40 || compare == 90 || compare == 400 || compare == 900){
                    a2[i]=compare;
                    a[i+1]=0;
                    
                }
                else{
                    a2[i]=a[i];
            }
            }
            else{
                int second = a[i+1];
                int first = a[i];
                int compare= second-first;
                if(compare==4 || compare ==9 || compare== 40 || compare == 90 || compare == 400 || compare == 900){
                    a2[i]=second-first;
                    a[i+1]=0;
                }
                else{
                    a2[i]=a[i];
                }
            }
        }
        }
        return a2;
    }
    public int addAll(int []a){
        int sum =0;
        for(int n: a){
            sum+=n;
        }
        return sum;
    }


}
    
