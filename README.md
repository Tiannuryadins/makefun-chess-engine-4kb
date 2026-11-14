# MiniMax-4K — Chess Engine in 4 KB of Python

A complete, legal chess engine in a single `main.py` of **4071 bytes**
(limit: 4096). No dependencies beyond the Python 3 standard library.

## How it plays

- **Board:** 120-square mailbox board (0x88-style), full legal move
  generation: castling (with real FEN castling rights), en passant,
  all four promotions (Q/R/B/N).
- **Search:** negamax + alpha-beta pruning, iterative deepening with a
  time budget, quiescence search over captures, MVV-LVA capture
  ordering, mate-distance scoring.
- **Evaluation:** material values + piece-square tables (pawn, knight,
  bishop/queen, rook, king) stored as compact byte strings.
- **Strength:** reaches depth 4 from the start position in ~0.9 s
  (~22.5k nodes); finds mate-in-1 and simple tactics (e.g. Scholar's
  mate) immediately. Move generation is verified correct by perft on
  the 6 standard test positions (see `BUILD-TRANSCRIPT.md`).

## Running it

```sh
python3 main.py "<FEN>" [seconds]
```

- `<FEN>` — a standard FEN string (full FEN preferred; a bare
  placement string is also accepted and treated as White to move).
- `[seconds]` — thinking time per move, default `2`.

Without arguments it reads from stdin instead: line 1 is the FEN,
optional line 2 is the thinking time in seconds.

```sh
echo "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" | python3 main.py
```

Requires Python 3.8+ (uses only `sys` and `time`).

## Input / output protocol

- **Input:** one FEN position per run (argv or stdin), plus an optional
  time budget in seconds.
- **Output:** exactly one line on stdout — the best move in
  coordinate (UCI) notation, e.g. `e2e4`, `e1g1` (castling),
  `e5d6` (en passant), `a7a8q` (promotion, with `q`/`r`/`b`/`n`
  suffix). The move is always legal for the given position.
- **No legal move** (checkmate or stalemate): outputs `0000`.
- Nothing else is printed to stdout; the program exits 0.

## Known limitations

- No draw detection by repetition or the fifty-move rule, no opening
  book, no endgame tablebase, single-threaded.
- Strength is bounded by the 4 KB size limit: plain alpha-beta
  without a transposition table.
