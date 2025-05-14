import React, { useState, useRef } from "react";
import BarcodeScannerComponent from "react-qr-barcode-scanner";
import axios from "axios";
import "./BarcodeReader.css";

const BarcodeReader = () => {
    const [barcode, setBarcode] = useState(null);
    const [product, setProduct] = useState(null);
    const [error, setError] = useState(null);
    const lastScanned = useRef(null);

    const handleScan = async (err, result) => {
        if (result && result.text !== lastScanned.current) {
            const code = result.text;
            lastScanned.current = code;
            setBarcode(code);
            setProduct(null);
            setError(null);

            try {
                const response = await axios.get(`https:/admin.karlearr.com/api/v1/products/${code}`);
                setProduct(response.data);
            } catch (e) {
                if (e.response?.status === 404) {
                    setError("Товар не найден");
                } else {
                    setError(`${e}`);
                }
            }
        }
    };

    return (
        <div className="scanner-wrapper">
            <div className="scanner-container">
                <h2>Сканер штрихкодов</h2>
                <BarcodeScannerComponent
                    width={280}
                    height={280}
                    onUpdate={handleScan}
                />
                {barcode && <p className="result-text">Штрихкод: {barcode}</p>}
                {error && <p className="error-text">{error}</p>}
                {product && (
                    <div className="product-info">
                        <p><strong>Артикул:</strong> {product.sku}</p>
                        <p><strong>Наименование:</strong> {product.name}</p>
                        <p><strong>Цена до:</strong> {product.old_price} ₽</p>
                        <p><strong>Цена после:</strong> {product.new_price} ₽</p>
                    </div>
                )}
            </div>
        </div>
    );
};

export default BarcodeReader;
