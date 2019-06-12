print("Enter no");
$no=<>;
$sum=0;
$temp=$no;
while($no!=0)
{
$rem=$no%10;
$sum=$sum+($rem*$rem*$rem);
$no=$no/10;
}
print("$sum");
if($temp==$sum)
{
print("armstrong");
}
else
{
print("NOT arm");
}
