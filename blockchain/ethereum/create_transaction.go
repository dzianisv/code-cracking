func constructTransaction(owner, contract, data string) string {
	amount := big.NewInt(0)
	gasLimit := uint64(0)
	gasPrice := big.NewInt(0)
	txData := []byte(data)

	tx := types.NewTransaction(1, common.HexToAddress(contract), amount, gasLimit, gasPrice, txData)
	ts := types.Transactions{tx}
	buffer := &bytes.Buffer{}
	ts.EncodeIndex(0, buffer)
	return hex.EncodeToString(buffer.Bytes())
}
