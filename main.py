def estimate_gas_fee(tx_type, congestion):
    base_gas = {'transfer': 21000, 'swap': 100000}
    congestion_multiplier = {'low': 1.0, 'medium': 1.2, 'high': 1.5}
    gwei_price = 20 # 1 birim gaz için Gwei fiyatı (temsili)

    if tx_type not in base_gas or congestion not in congestion_multiplier:
        return "Geçersiz işlem tipi veya yoğunluk seviyesi."

    estimated_gas = base_gas[tx_type] * congestion_multiplier[congestion]
    fee_in_gwei = estimated_gas * gwei_price
    fee_in_eth = fee_in_gwei / 1_000_000_000 # 1 Eth = 1 milyar Gwei
    
    return f"Tahmini Ücret: {fee_in_eth:.6f} ETH"

if __name__ == "__main__":
    print("Düşük yoğunlukta normal transfer ücreti:", estimate_gas_fee('transfer', 'low'))
    print("Yüksek yoğunlukta bir swap işlemi ücreti:", estimate_gas_fee('swap', 'high'))