; Pseudo-assembly for allocating memory (using registers for addresses)
ALLOCATE_MEM:
    ; Register R0 holds the required size
    ; Check if enough free space is available
    ; Store memory pointer in R1, size in R2
    MOV R1, MEMORY_POINTER
    MOV R2, ALLOCATED_SIZE
    RET
