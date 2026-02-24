# Finance Rules & Logic

## 🏦 Entity Structure
- **Personal:** Gary Inc. (W2, Living Expenses)
- **Business:** Ef Enterprises (Consulting, Apps, AI)
- **Real Estate:** Rental Portfolio (Tampa Duplex)

## 📊 Monthly Budgets
| Category | Budget | Notes |
| :--- | :--- | :--- |
| **Personal Total** | **$5,200** | Strict Cap |
| Housing | Included | Mortgage/Rent share |
| Food/Dining | Included | |
| Counseling | Included | Non-negotiable |
| **Business Total** | **$2,900** | OpEx Cap |

## 💡 Utility Split Protocols (Tampa Duplex)
| Utility | Split Rule | Tenant Responsibility | Owner Responsibility |
| :--- | :--- | :--- | :--- |
| **Water** | 50/50 | 50% of total bill | 50% (Vacancy/Owner) |
| **Trash/Sewage** | 1/3 per unit | 33% (Unit 1), 33% (Unit 2) | 33% (Owner/Common) |
| **Gas** | 50/50 | 50% of total bill | 50% |
| **Electric** | Metered | 100% of Unit Meter | Common Areas only |
| **Internet** | 50/50 | 50% (if shared) | 50% |

**Special Credits:**
- **Unit 2 Credit:** $150.00/month applied to rent/utilities.

## 💳 Account Mappings (SimleFIN)
- **Chase Sapphire Reserve:** Personal (Travel/Dining)
- **Amex Platinum:** Business (Software/Flights)
- **Ally Bank:** Emergency Fund / Savings
- **NFCU:** Real Estate checking
- **Robinhood:** Investments

## 🔄 Automation Rules
1. **Transaction Arrival:** Daily sync via SimpleFIN.
2. **Categorization:** Python script maps merchant -> Entity -> Category.
3. **Ambiguity:** If confidence < 80%, flag as "Requires Triage" in Google Sheet.
4. **Dashboard Update:** Push `finance.json` to GitHub Pages immediately after sync.
