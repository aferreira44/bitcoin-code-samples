# BDK

## Introduction


https://bitcoindevkit.org/
https://bitcoindevkit.org/bdk-cli/
https://bitcoindevkit.org/bdk-cli/playground/
https://bitcoin.sipa.be/miniscript/
https://bitcoindevkit.org/descriptors/

https://web.archive.org/web/20211028083245/https://bitcoindevkit.org/blog/2021/02/spending-policy-demo/
https://twitter.com/notmandatory
https://www.youtube.com/watch?v=2DMnyXLIfCI&list=PLmyfVqsSelG3jSobvpY3GoNKDtAumsrg3&index=2

Descriptors: define how and when to spend the outputs of a transaction (e.g. 2 of 2, 2 of 3, timelock, etc.)

- Electrum
- Neutrino
- Bitcoin RPC
- Esplora

- **PSBT**: Partially Signed Bitcoin Transaction

## Step 0: Install a recent version bdk-cli

- `cargo install bdk-cli --features repl,electrum,compiler`
- `bdk-cli --help`

## Step 1: Generate private extended keys

- `bdk-cli key generate | tee alice-key.json`
- `bdk-cli key generate | tee bob-key.json`
- `bdk-cli key generate | tee carol-key.json`

## Step 2: Extract private extended keys

- `export ALICE_XPRV=$(cat alice-key.json | jq -r '.xprv')`
- `export BOB_XPRV=$(cat bob-key.json | jq -r '.xprv')`
- `export CAROL_XPRV=$(cat carol-key.json | jq -r '.xprv')`

## Step 3: Derive public extended keys

- `export ALICE_XPUB=$(bdk-cli key derive --xprv $ALICE_XPRV --path "m/84'/1'/0'/0" | jq -r ".xpub")`
- `export BOB_XPUB=$(bdk-cli key derive --xprv $BOB_XPRV --path "m/84'/1'/0'/0" | jq -r ".xpub")`
- `export CAROL_XPUB=$(bdk-cli key derive --xprv $CAROL_XPRV --path "m/84'/1'/0'/0" | jq -r ".xpub")`

## Step 4: Create wallet descriptors for each participant

- `export ALICE_DESCRIPTOR=$(bdk-cli compile "thresh(3,pk($ALICE_XPRV/84'/1'/0'/0/*),pk($BOB_XPUB),pk($CAROL_XPUB),older(2))" | jq -r ".descriptor")`
- `export BOB_DESCRIPTOR=$(bdk-cli compile "thresh(3,pk($ALICE_XPUB),pk($BOB_XPRV/84'/1'/0'/0/*),pk($CAROL_XPUB),older(2))" | jq -r ".descriptor")`
- `export CAROL_DESCRIPTOR=$(bdk-cli compile "thresh(3,pk($ALICE_XPUB),pk($BOB_XPUB),pk($CAROL_XPRV/84'/1'/0'/0/*),older(2))" | jq -r ".descriptor")`

## Step 5: Create a testnet segwit receive address for each participant

- `rm -rf ~/.bdk-bitcoin`
- `bdk-cli wallet -w alice -d $ALICE_DESCRIPTOR get_new_address`

tb1qc9vlja947uzk25zc0lm49tdmhaxgumqfmg5jd5ntwfr07juesklsneynvw

- `bdk-cli wallet -w bob -d $BOB_DESCRIPTOR get_new_address`

tb1qc9vlja947uzk25zc0lm49tdmhaxgumqfmg5jd5ntwfr07juesklsneynvw

- `bdk-cli wallet -w carol -d $CAROL_DESCRIPTOR get_new_address`

tb1qc9vlja947uzk25zc0lm49tdmhaxgumqfmg5jd5ntwfr07juesklsneynvw

## Step 6: Check if it's an unused address

- `bdk-cli wallet -w alice -d $ALICE_DESCRIPTOR sync`
- `bdk-cli wallet -w alice -d $ALICE_DESCRIPTOR get_balance`
- `bdk-cli wallet -w alice -d $ALICE_DESCRIPTOR list_transactions`

- `bdk-cli wallet -w bob -d $BOB_DESCRIPTOR sync`
- `bdk-cli wallet -w bob -d $BOB_DESCRIPTOR get_balance`
- `bdk-cli wallet -w bob -d $BOB_DESCRIPTOR list_transactions`

- `bdk-cli wallet -w carol -d $CAROL_DESCRIPTOR sync`
- `bdk-cli wallet -w carol -d $CAROL_DESCRIPTOR get_balance`
- `bdk-cli wallet -w carol -d $CAROL_DESCRIPTOR list_transactions`

## Step 7: Fund the wallet for each participant

https://bitcoinfaucet.uo1.net/send.php

- **Alice:** https://mempool.space/testnet/address/tb1qc9vlja947uzk25zc0lm49tdmhaxgumqfmg5jd5ntwfr07juesklsneynvw
- **Bob:** https://mempool.space/testnet/address/tb1qc9vlja947uzk25zc0lm49tdmhaxgumqfmg5jd5ntwfr07juesklsneynvw
- **Carol:** https://mempool.space/testnet/address/tb1qc9vlja947uzk25zc0lm49tdmhaxgumqfmg5jd5ntwfr07juesklsneynvw

## Step 6: Check the balance of the wallet for each participant

- `bdk-cli wallet -w alice -d $ALICE_DESCRIPTOR sync`
- `bdk-cli wallet -w alice -d $ALICE_DESCRIPTOR get_balance`
- `bdk-cli wallet -w alice -d $ALICE_DESCRIPTOR list_transactions`

- `bdk-cli wallet -w bob -d $BOB_DESCRIPTOR sync`
- `bdk-cli wallet -w bob -d $BOB_DESCRIPTOR get_balance`
- `bdk-cli wallet -w bob -d $BOB_DESCRIPTOR list_transactions`

- `bdk-cli wallet -w carol -d $CAROL_DESCRIPTOR sync`
- `bdk-cli wallet -w carol -d $CAROL_DESCRIPTOR get_balance`
- `bdk-cli wallet -w carol -d $CAROL_DESCRIPTOR list_transactions`

## Step 7: View wallet spending policies

- `bdk-cli wallet -w alice -d $ALICE_DESCRIPTOR policies`

## Step 8: Create a PSBT transaction from Alice to Carol

`export UNSIGNED_PSBT=$(bdk-cli wallet -w alice -d $ALICE_DESCRIPTOR create_tx -a --to tb1qm5tfegjevj27yvvna9elym9lnzcf0zraxgl8z2:0 --external_policy "{\"x8deynnj\": [0,1,2]}" | jq -r ".psbt")`







