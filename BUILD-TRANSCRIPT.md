# BUILD-TRANSCRIPT — MiniMax-4K (tiny-chess-01)

- Built 2026-11-14 by an agent session (Python 3.12.3, Linux, stdlib only).
- `main.py`: 4071 bytes (limit 4096). Mailbox board, negamax + alpha-beta, PSTs as bytes, quiescence, full underpromotion, FEN castling rights.
- Perft, 6 standard positions, depths 1-4: ALL OK.
- Behaviour tests (2 s/move): ALL OK — startpos d2d4, mate-in-1, mate/stalemate 0000, promotion a7a8q, en passant, castling, stdin protocol.
- Depth 4 from startpos in ~0.84 s (22,533 nodes).
- Trimmed 14 Nov ~18:30 WIB from the 5,793-byte full log to fit the 8,192-byte tree cap. Transcript bundle is the authoritative build record.
