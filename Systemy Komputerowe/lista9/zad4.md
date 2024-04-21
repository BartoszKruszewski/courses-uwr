#### Tagged Hybrid Predictors

Predykatory TAGE łączy w sobie wiele predykatorów globalnych o historiach różnej długości.

#### Działanie

Działa za pomocą hashowania jak gshare, z tą różnicą, że adresy hashowania mogą być krótkie i nie być w 100% dokładne. Predykator stara się dopasować hashowanie do wartości z predykatorów globalnych, natomiast jeżeli jest to niemożliwe to korzysta z predykatora domyślnego.

#### Efektywność

Predykatory TAGE mają bardzo wysoką efektywność, porównując je z innymi predykatorami uwzględniając wielkości pamięci rzędu ponad 32KB. Ich wadą jest długi okres nasycania, podczas którego nie osiągają pełnych możliwości. Predykator najpierw wykonuje przewidywania z duża ilością błędów, które w miare uzupełniania historii występują coraz rzadziej.
