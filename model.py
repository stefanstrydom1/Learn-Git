def premium_calculation(frequency: float, severity: float, target_loss_ratio: float):
    expected_loss = frequency * severity
    technical_premium = expected_loss / target_loss_ratio
    return expected_loss, technical_premium