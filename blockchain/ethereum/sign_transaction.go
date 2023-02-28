package server_test

import (
	"bytes"
	"encoding/hex"
	"fmt"
	"math/big"

	"github.com/ethereum/go-ethereum/core/types"
	"github.com/ethereum/go-ethereum/crypto"
	"github.com/ethereum/go-ethereum/rlp"
)

const (
	NetworkId = 5
)

func SignEthTransaction(rawUnsignedTransaction string, privateKeyHex string) (string, error) {

	privateKey, err := crypto.HexToECDSA(privateKeyHex)
	if err != nil {
		return "", err
	}

	// https://goethereumbook.org/transaction-raw-create/
	rawTxBytes, err := hex.DecodeString(rawUnsignedTransaction)
	if err != nil {
		return "", fmt.Errorf("Failed to DecodeString %s: %w", rawUnsignedTransaction, err)
	}
	tx := new(types.Transaction)
	err = rlp.DecodeBytes(rawTxBytes, &tx)
	if err != nil {
		return "", err
	}

	signedTx, err := types.SignTx(tx, types.NewEIP155Signer(big.NewInt(NetworkId)), privateKey)
	if err != nil {
		return "", err
	}

	ts := types.Transactions{signedTx}
	buffer := &bytes.Buffer{}
	ts.EncodeIndex(0, buffer)

	rawTx := hex.EncodeToString(buffer.Bytes())
	return rawTx, nil
}
