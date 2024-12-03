{

                            Online Pascal Compiler.
                Code, Compile, Run and Debug Pascal program online.
Write your code in this editor and press "Run" button to execute it.

}


Program Day1AdventofCode;

Uses Crt;

Const length= 6;

Type
Tableau = Array [1..length] of Integer;

Procedure Saisie (var Tab : Tableau);
Var i : Integer;
Begin
for i := 1 to length do
begin
Write('Entrez la valeur de la case n°',i,' : ');
ReadLn(Tab[i]);
end;
End;

{ Fonction Tri (pourquoi n'y a t il pas de fonction native ??)}
Procedure Tri (var Tab : Tableau);
Var i, j, temp : Integer;
begin
  for i := Low(Tab) to High(Tab) - 1 do
    for j := i + 1 to High(Tab) do
      if Tab[i] > Tab[j] then
      begin
        temp := Tab[i];
        Tab[i] := Tab[j];
        Tab[j] := temp;
      end;
end;

{ Fonction pour compter les occurrences (idem pourquoi je ne peux pas faire un .occurence()? }
function CountOccurrences(Tab: Tableau; x: Integer): Integer;
var
  i, count: Integer;
begin
  count := 0;
  for i := Low(Tab) to High(Tab) do
    if tab[i] = x then
      Inc(count);
  CountOccurrences := count;
end;

{ Fonction afficher (on dirait du C vite fait) }
Procedure Affiche (var Tab : Tableau);
Var i : Integer;
Begin
for i := 1 to length do Write(Tab[i],' ');
WriteLn;
End;

{ C'est parti pour les 20 points}

var
  Tab1, Tab2, Tri_Tab1, Tri_Tab2: Tableau;
  i, max_len, absolute_distance, similarity_score: Integer;
  occurrences: Tableau;
  
begin
ClrScr;
  { Saisir les listes (j'ai pas trouvé read_csv() }
  Saisie(Tab1);
  Saisie(Tab2);

  { Part 1 Etape 1: Trier les listes }
  Tri_Tab1 := Tab1;
  Tri_Tab2 := Tab2;
  Tri(Tri_Tab1);
  Tri(Tri_Tab2 );

{ Partie 1 Etape 2: Calculer la norme de L1 dite de Manhattan }
 absolute_distance := 0;
 for i := Low(Tri_Tab1) to High(Tri_Tab1) do
    absolute_distance := absolute_distance + Abs(Tri_Tab1[i] - Tri_Tab2[i]);

 WriteLn('Normed Absolute Distance: ', absolute_distance);
 
  { Partie 2 Step 1: Norme de similarité = l1.occurrences(l1 in l2) }

  for i := Low(Tab1) to High(Tab2) do
    occurrences[i] := CountOccurrences(Tab2, Tab1[i]);

  similarity_score := 0;
  for i := Low(Tab1) to High(Tab1) do
    similarity_score := similarity_score + Tab1[i] * occurrences[i];

  WriteLn('Similarity Score: ', similarity_score);
end.

