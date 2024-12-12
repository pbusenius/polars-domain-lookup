import polars as pl
from polars_domain_lookup import is_common_domain


df = pl.DataFrame(
    {
        "dns": ["github.com", "google.de", "blub.com", "heise.de"],
    }
)

result = df.with_columns(is_common_domain=is_common_domain("dns"))
print(result)
