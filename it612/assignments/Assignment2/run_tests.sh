#!/bin/bash
# =============================================================================
# Assignment 2: Basic Bash — Test Runner
#
# Runs all four exercises, checks output, and generates results.txt
# Usage: bash run_tests.sh
# =============================================================================

RESULTS="results.txt"
PASS=0
FAIL=0
TOTAL=0

# --- Helpers -----------------------------------------------------------------

divider() {
    echo "============================================================"
}

section() {
    echo ""
    divider
    echo "  $1"
    divider
}

show_code() {
    local file="$1"
    if [ -f "$file" ]; then
        echo ""
        echo "--- $file ---"
        cat "$file"
        echo "--- end $file ---"
    else
        echo ""
        echo "--- $file NOT FOUND ---"
    fi
}

check_test() {
    local name="$1"
    local expected="$2"
    local actual="$3"
    TOTAL=$((TOTAL + 1))
    if [ "$expected" = "$actual" ]; then
        echo "  [PASS] $name"
        PASS=$((PASS + 1))
    else
        echo "  [FAIL] $name"
        echo "    Expected: $(echo "$expected" | head -5)"
        echo "    Got:      $(echo "$actual" | head -5)"
        FAIL=$((FAIL + 1))
    fi
}

# --- Begin results -----------------------------------------------------------

{
    echo "Assignment 2: Basic Bash — Test Results"
    echo "Generated: $(date)"
    echo ""

    # =========================================================================
    # Exercise 1: Expensive Soda
    # =========================================================================
    section "Exercise 1: Expensive Soda"
    show_code "soda.sh"
    echo ""

    if [ -f "soda.sh" ]; then
        actual=$(bash soda.sh 2>/dev/null)
        expected='A soda costs $9?!'
        check_test "Output matches exactly" "$expected" "$actual"
    else
        TOTAL=$((TOTAL + 1)); FAIL=$((FAIL + 1))
        echo "  [FAIL] soda.sh not found"
    fi

    # =========================================================================
    # Exercise 2: Greetings
    # =========================================================================
    section "Exercise 2: Greetings"
    show_code "greetings.sh"
    echo ""

    if [ -f "greetings.sh" ]; then
        actual=$(bash greetings.sh 2>/dev/null)
        # The starter sets first_name=Jane, last_name=Doe
        expected=$(printf "Hello\nJane\tDoe\nHow are you?")
        check_test "Output matches with tab character" "$expected" "$actual"
    else
        TOTAL=$((TOTAL + 1)); FAIL=$((FAIL + 1))
        echo "  [FAIL] greetings.sh not found"
    fi

    # =========================================================================
    # Exercise 3: Mixed Messages
    # =========================================================================
    section "Exercise 3: Mixed Messages"
    show_code "mixed.sh"
    echo ""

    if [ -f "mixed.sh" ]; then
        actual_stdout=$(bash mixed.sh 2>/dev/null)
        actual_stderr=$(bash mixed.sh 2>&1 1>/dev/null)

        check_test "stdout is 'Everything is fine'" "Everything is fine" "$actual_stdout"
        check_test "stderr is 'WARNING: SEVERE ERROR'" "WARNING: SEVERE ERROR" "$actual_stderr"
    else
        TOTAL=$((TOTAL + 2)); FAIL=$((FAIL + 2))
        echo "  [FAIL] mixed.sh not found"
    fi

    # =========================================================================
    # Exercise 4: Read, Sort and Trim
    # =========================================================================
    section "Exercise 4: Read, Sort and Trim"
    show_code "pipeline.sh"
    echo ""

    if [ -f "pipeline.sh" ]; then
        # Clean up any previous run
        rm -f sorted.dat input.dat

        actual_stdout=$(bash pipeline.sh 2>/dev/null)

        # Check sorted.dat was created with correct content
        # Input: 3 2 10 5 100 25 12 13 6
        # Descending numeric sort: 100 25 13 12 10 6 5 3 2
        expected_sorted=$(printf "100\n25\n13\n12\n10\n6\n5\n3\n2")

        if [ -f "sorted.dat" ]; then
            actual_sorted=$(cat sorted.dat)
            check_test "sorted.dat exists with correct descending sort" "$expected_sorted" "$actual_sorted"
        else
            TOTAL=$((TOTAL + 1)); FAIL=$((FAIL + 1))
            echo "  [FAIL] sorted.dat was not created"
        fi

        # Stdout: skip first line (100), next 5 lines (25 13 12 10 6)
        expected_stdout=$(printf "25\n13\n12\n10\n6")
        check_test "stdout shows lines 2-6 of sorted result" "$expected_stdout" "$actual_stdout"

        # Clean up
        rm -f sorted.dat input.dat
    else
        TOTAL=$((TOTAL + 2)); FAIL=$((FAIL + 2))
        echo "  [FAIL] pipeline.sh not found"
    fi

    # =========================================================================
    # Summary
    # =========================================================================
    echo ""
    divider
    echo "  SUMMARY: $PASS/$TOTAL tests passed"
    if [ $FAIL -eq 0 ]; then
        echo "  All tests passed!"
    else
        echo "  $FAIL test(s) failed"
    fi
    divider

} | tee "$RESULTS"

echo ""
echo "Results saved to $RESULTS"
