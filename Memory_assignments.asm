; Pseudo-assembly for memory assignment
ASSIGN_MEMORY:
    ; R1 holds the memory pointer, R2 the value to assign
    MOV [R1], R2
    RET
