# Zero-Knowledge from Zero Knowledge

Companion code for the dev.to series. Every folder matches one post.

[**Blog series**](https://dev.to/grandpaarush/series/46898)

| Folder | Post | Language | Status | Blog |
|---|---|---|---|---|
| `01-cave` | What a ZK proof actually proves | Python 3 | ✅ runs | [Post 1](https://dev.to/grandpaarush/how-can-i-prove-i-know-a-secret-without-telling-you-the-secret-zero-knowledge-proofs-78o) |
| `02-quiz` | Where ZK is used | Python 3 | ✅ runs | [Post 2](https://dev.to/grandpaarush/what-is-zero-knowledge-actually-used-for-10l6) |
| `03-merkle-tree` | Hashes, commitments and Merkle trees | Python 3 (stdlib) | ✅ runs | [Post 3](https://dev.to/grandpaarush/how-do-you-prove-something-is-in-a-list-without-sharing-the-whole-list-529d) |

## Tooling

Tested with `nargo 1.0.0`, `bb 6.0.0`, `circom 2.2.3`, `snarkjs 0.7`, `forge 1.9.0` (solc 0.8.38) and Python 3.12.

```bash
# Noir
curl -L https://raw.githubusercontent.com/noir-lang/noirup/refs/heads/main/install | bash
noirup

# Barretenberg (the proving backend, `bb`)
curl -L https://raw.githubusercontent.com/AztecProtocol/aztec-packages/refs/heads/next/barretenberg/bbup/install | bash
bbup

# Circom (needs Rust) + snarkjs: see https://docs.circom.io/getting-started/installation/
cargo install --git https://github.com/iden3/circom.git
npm install -g snarkjs

# Foundry
curl -L https://foundry.paradigm.xyz | bash
foundryup
```