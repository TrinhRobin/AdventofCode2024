{

                            Online Pascal Compiler.
                Code, Compile, Run and Debug Pascal program online.
Write your code in this editor and press "Run" button to execute it.

}

Program day2;
Uses
Crt, Dos,Math;

const
  MaxRows = 10000; { Maximum number of lines }
  MaxCols = 10;  { Maximum number of elements per line }

type
  StringArray = array[1..MaxCols] of String;
   IntArray = array[1..MaxCols] of Integer;
  ListOfLists = array[1..MaxRows] of IntArray;
 
  
Var
inputFile : Text;{ File variable for the text file }
line, element: String;       { Variable to store each line read }
elementIndex: Integer;

Choix : Char;
list: ListOfLists;
row, col: Integer;

var
  listex: IntArray;

  isIncreasing: Boolean;


{ Function to split a string into an array of strings by delimiter }
function SplitString(s: String; delimiter: Char; var elements: IntArray): Integer;
var
  posStart, posEnd, idx,num: Integer;
  temp: String;
begin
  posStart := 1;
  idx := 0;

  repeat
    posEnd := Pos(delimiter, s);
    if posEnd = 0 then
      posEnd := Length(s) + 1;

    Inc(idx);
    temp := Copy(s, posStart, posEnd - posStart);
    Val(temp,num);
    elements[idx] := num;
    Delete(s, 1, posEnd);

  until s = '';

  SplitString := idx; { Return the number of elements }
end;
 
Procedure Lecture;
begin
  { Assign the file to the file variable }
  Assign(inputFile, 'day2.txt');  

  { Open the file for reading }
  Reset(inputFile);

  { Read the file line by line }
  while not EOF(inputFile) do
  begin
    ReadLn(inputFile, line);  { Read a line from the file }
    WriteLn('Read line: ', line);  { Process or display the line }
    Inc(row); { Move to the next row }
    { Split the line into elements and store them }
    col := SplitString(line, ' ', list[row]);
  end;

  { Close the file }
  Close(inputFile);
end;

Procedure DisplayListofList;
begin;
{ Display the list of lists }
  WriteLn('File Content as List of Lists:');
  for row := 1 to row do
  begin
    Write('Row ', row, ': ');
    for col := 1 to MaxCols do
    begin
      Write(list[row][col], ' ');
    end;
    WriteLn;
  end;
end;

procedure DisplayList(list: IntArray);
var
  i: Integer;
begin
  Write('List: [');
  for i := Low(list) to High(list) do
  begin
    Write(list[i]);
    if i < High(list) then
      Write(', ');
  end;
  WriteLn(']');
end;


{ Function to check if x < y and the difference is between 1 and 3 }
function SafeCombinationElement1(x, y: Integer): Boolean;
begin
  SafeCombinationElement1 := (x < y) and (Abs(x - y) >= 1) and (Abs(x - y) <= 3);
end;

{ Function to check if x > y and the difference is between 1 and 3 }
function SafeCombinationElement2(x, y: Integer): Boolean;
begin
  SafeCombinationElement2 := (x > y) and ( Abs(x - y) >= 1) and ( Abs(x - y) <= 3);
end;

function SafeCombinationList(list: IntArray): Boolean;
var
  i: Integer;
begin
  SafeCombinationList := True; { Assume the list is safe initially }
  {DisplayList(list);}
    For i := Low(list) to High(list) do
    
    if  (list[i]>0) and (list[i+1]>0) then
    begin
    if not (SafeCombinationElement1(list[i], list[i+1]) or
              SafeCombinationElement2(list[i], list[i+1]))
              then 
begin

{writeln('condition1',SafeCombinationElement1(list[i], list[i+1]),'abs',Abs(list[i] - list[i-1]));
writeln('condition2',SafeCombinationElement2(list[i], list[i+1]),'abs',Abs(list[i] - list[i-1]));
}
SafeCombinationList := False;
Exit; { Exit as soon as a violation is found }
end;
end;
end;

function  CountSafeCombinations(ll:ListOfLists):Integer;
var
  i, count: Integer;
 begin
  count := 0;
  for i := 1 to row do

  WriteLn('i : ',SafeCombinationList(ll[i]));
  if SafeCombinationList(ll[i]) then
        WriteLn('count:',count);
      Inc(count);
CountSafeCombinations := count;
 end;

{ Function to count safe combinations in a list of lists }
function CountSafeCombinations2(ll: ListOfLists; numRows, numCols: Integer): Integer;
var
  i, j: Integer;
  isSafe: Boolean;
  count: Integer;
begin
  count := 0;

  { Iterate through each list }
  for i := 1 to numRows do
  begin
    isSafe := True;

    { Check each pair of adjacent elements in the current list }
    for j := 1 to numCols - 1 do
    begin
      { Check if either condition is met }
      if (ll[i][j]>0) and (ll[i][j+1]>0)  and not (SafeCombinationElement1(ll[i][j], ll[i][j + 1]) or
              SafeCombinationElement2(ll[i][j], ll[i][j + 1])) then
      begin
        isSafe := False;
        Break; { Exit inner loop if any combination is unsafe }
      end;
    end;

    { Increment the count if the list is safe }
    if isSafe then
      Inc(count);
  end;

  CountSafeCombinations2 := count; { Return the total count }
end;

var
  solution_part1: Integer;
 var
 i:Integer;

{ Main program for testing }
BEGIN
Clrscr;
Write('Voulez-vous lire le fichier init.txt ? [O/N] ');
Choix := ReadKey;
if (UpCase(Choix) = 'O') then Lecture;
DisplayListofList;

solution_part1 := 0;

solution_part1:= CountSafeCombinations2(list, 10000, 10); {CountSafeCombinations(list);}
WriteLn('Number of Safe Combinations: ', solution_part1);


{begin
  
  listex[1] := 1; listex[2] := 3; listex[3] := 5; listex[4] := 7;

  if  SafeCombinationList(listex) then
    WriteLn('The list is safe.')
  else
    WriteLn('The list is not safe.');
end;
}

end.