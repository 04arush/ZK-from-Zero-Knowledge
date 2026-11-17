# Zero-Knowledge from Zero Knowledge

Companion code for the dev.to series. Every folder matches one post.

| Folder | Post | Language | Status |
|---|---|---|---|
| `01-cave` | What a ZK proof actually proves | Python 3 | ✅ runs |

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