; NOTE: Assertions have been autogenerated by utils/update_llc_test_checks.py
; RUN: llc -O0 -mtriple=mipsel-unknown-linux-gnu -mcpu=mips32r2 -target-abi=o32 < %s -filetype=asm -o - \
; RUN:   | FileCheck -check-prefixes=O32 %s
; RUN: llc -O0 -mtriple=mips64el-unknown-linux-gnu -mcpu=mips64r2 -target-abi=n32 < %s -filetype=asm -o - \
; RUN:   | FileCheck  -check-prefixes=N32,ALL %s
; RUN: llc -O0 -mtriple=mips64el-unknown-linux-gnu -mcpu=mips64r2 -target-abi=n64 < %s -filetype=asm -o - \
; RUN:   | FileCheck -check-prefixes=N64 %s

@sym = external global i32 *

define void @foo(i32 %new, i32 %old) {
; O32-LABEL: foo:
; O32:       # %bb.0: # %entry
; O32-NEXT:    addiu $sp, $sp, -16
; O32-NEXT:    .cfi_def_cfa_offset 16
; O32-NEXT:    move $1, $5
; O32-NEXT:    move $2, $4
; O32-NEXT:    lui $3, %hi(sym)
; O32-NEXT:    lw $3, %lo(sym)($3)
; O32-NEXT:    sync
; O32-NEXT:    lw $6, 12($sp) # 4-byte Folded Reload
; O32-NEXT:  $BB0_1: # %entry
; O32-NEXT:    # =>This Inner Loop Header: Depth=1
; O32-NEXT:    ll $7, 0($3)
; O32-NEXT:    bne $7, $4, $BB0_3
; O32-NEXT:    nop
; O32-NEXT:  # %bb.2: # %entry
; O32-NEXT:    # in Loop: Header=BB0_1 Depth=1
; O32-NEXT:    move $8, $5
; O32-NEXT:    sc $8, 0($3)
; O32-NEXT:    beqz $8, $BB0_1
; O32-NEXT:    nop
; O32-NEXT:  $BB0_3: # %entry
; O32-NEXT:    sync
; O32-NEXT:    sw $1, 8($sp) # 4-byte Folded Spill
; O32-NEXT:    sw $2, 4($sp) # 4-byte Folded Spill
; O32-NEXT:    sw $7, 12($sp) # 4-byte Folded Spill
; O32-NEXT:    sw $6, 0($sp) # 4-byte Folded Spill
; O32-NEXT:    addiu $sp, $sp, 16
; O32-NEXT:    jr $ra
; O32-NEXT:    nop
;
; N32-LABEL: foo:
; N32:       # %bb.0: # %entry
; N32-NEXT:    addiu $sp, $sp, -16
; N32-NEXT:    .cfi_def_cfa_offset 16
; N32-NEXT:    move $1, $5
; N32-NEXT:    sll $1, $1, 0
; N32-NEXT:    move $2, $4
; N32-NEXT:    sll $2, $2, 0
; N32-NEXT:    lui $3, %hi(sym)
; N32-NEXT:    lw $3, %lo(sym)($3)
; N32-NEXT:    sync
; N32-NEXT:    lw $6, 12($sp) # 4-byte Folded Reload
; N32-NEXT:  .LBB0_1: # %entry
; N32-NEXT:    # =>This Inner Loop Header: Depth=1
; N32-NEXT:    ll $7, 0($3)
; N32-NEXT:    bne $7, $2, .LBB0_3
; N32-NEXT:    nop
; N32-NEXT:  # %bb.2: # %entry
; N32-NEXT:    # in Loop: Header=BB0_1 Depth=1
; N32-NEXT:    move $8, $1
; N32-NEXT:    sc $8, 0($3)
; N32-NEXT:    beqz $8, .LBB0_1
; N32-NEXT:    nop
; N32-NEXT:  .LBB0_3: # %entry
; N32-NEXT:    sync
; N32-NEXT:    sw $7, 12($sp) # 4-byte Folded Spill
; N32-NEXT:    sw $6, 8($sp) # 4-byte Folded Spill
; N32-NEXT:    addiu $sp, $sp, 16
; N32-NEXT:    jr $ra
; N32-NEXT:    nop
;
; N64-LABEL: foo:
; N64:       # %bb.0: # %entry
; N64-NEXT:    daddiu $sp, $sp, -16
; N64-NEXT:    .cfi_def_cfa_offset 16
; N64-NEXT:    move $1, $5
; N64-NEXT:    sll $1, $1, 0
; N64-NEXT:    move $2, $4
; N64-NEXT:    sll $2, $2, 0
; N64-NEXT:    lui $4, %highest(sym)
; N64-NEXT:    daddiu $4, $4, %higher(sym)
; N64-NEXT:    dsll $4, $4, 16
; N64-NEXT:    daddiu $4, $4, %hi(sym)
; N64-NEXT:    dsll $4, $4, 16
; N64-NEXT:    ld $4, %lo(sym)($4)
; N64-NEXT:    sync
; N64-NEXT:    lw $3, 12($sp) # 4-byte Folded Reload
; N64-NEXT:  .LBB0_1: # %entry
; N64-NEXT:    # =>This Inner Loop Header: Depth=1
; N64-NEXT:    ll $6, 0($4)
; N64-NEXT:    bne $6, $2, .LBB0_3
; N64-NEXT:    nop
; N64-NEXT:  # %bb.2: # %entry
; N64-NEXT:    # in Loop: Header=BB0_1 Depth=1
; N64-NEXT:    move $7, $1
; N64-NEXT:    sc $7, 0($4)
; N64-NEXT:    beqz $7, .LBB0_1
; N64-NEXT:    nop
; N64-NEXT:  .LBB0_3: # %entry
; N64-NEXT:    sync
; N64-NEXT:    sw $6, 12($sp) # 4-byte Folded Spill
; N64-NEXT:    sw $3, 8($sp) # 4-byte Folded Spill
; N64-NEXT:    daddiu $sp, $sp, 16
; N64-NEXT:    jr $ra
; N64-NEXT:    nop
entry:
  %0 = load i32 *, i32 ** @sym
  cmpxchg i32 * %0, i32 %new, i32 %old seq_cst seq_cst
  ret void
}
