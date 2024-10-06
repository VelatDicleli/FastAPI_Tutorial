from typing import Annotated
from fastapi import Depends

# Bağımlılığı temsil eden asenkron fonksiyon
async def dependency_a():
    dep_a = generate_dep_a()  # generate_dep_a() fonksiyonu ile dep_a yaratılır
    try:
        yield dep_a  # dep_a'yı kullanıma sunar
    finally:
        dep_a.close()  # Bağımlılık kullanıldıktan sonra kapatılır

# Bağımlılığı temsil eden asenkron fonksiyon
async def dependency_b(dep_a: Annotated[DepA, Depends(dependency_a)]):
    dep_b = generate_dep_b()  # generate_dep_b() fonksiyonu ile dep_b yaratılır
    try:
        yield dep_b  # dep_b'yi kullanıma sunar
    finally:
        dep_b.close(dep_a)  # dep_b kapatılırken dep_a'ya ihtiyaç duyabilir

# Bağımlılığı temsil eden asenkron fonksiyon
async def dependency_c(dep_b: Annotated[DepB, Depends(dependency_b)]):
    dep_c = generate_dep_c()  # generate_dep_c() fonksiyonu ile dep_c yaratılır
    try:
        yield dep_c  # dep_c'yi kullanıma sunar
    finally:
        dep_c.close(dep_b)  # dep_c kapatılırken dep_b'ye ihtiyaç duyabilir
