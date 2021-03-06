#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 08:11:39 2020

@author: jeanwolf
"""
import xlrd
import pandas as pd
# Abrimos el fichero excel
# Luego Leer las celdas del libro de nombres 
# contenido_celda = Sheet1.cell_value(x,x) (tratar de hacer un for)

document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919711-0-E - F400_.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a001  =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919724-0-E - F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a002 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919736-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a003 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919740-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a004 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919741-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a005 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919750-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a006 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919757-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a007 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919760-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a008 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919763-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a009 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919764-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a010 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919768-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a011 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919769-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a012 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919774-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a013 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919775-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a014 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919777-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a015 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919779-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a016 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919780-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a017 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919781-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a018 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919792-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a019 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919795-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a020 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919801-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a021 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919806-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a022 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-919811-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a023 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-924489-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a024 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-926869-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a025 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-936445-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a026 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-943315-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a027 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-953408-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a028 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-955180-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
# t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
# t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
# t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
# t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
# t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a029 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-957633-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
# t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
# t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
# t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
# t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
# t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a030 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-957635-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
# t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
# t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
# t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
# t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
# t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a031 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-957640-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
# t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a032 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-958721-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a033 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-960146-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
# t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
# t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
# t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
# t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
# t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a034 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-960196-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a035 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-960213-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a036 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-961473-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a037 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-965507-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a038 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-967683-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
# t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
# t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
# t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
# t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
# t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a039 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-970415-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a040 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-970431-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a041 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-973553-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
# t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a042 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-974510-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a043 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-974552-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a044 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-974596-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a045 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-974608-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a046 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-974615-0-EF400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a047 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-974663-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a048 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-979671-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a049 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-980870-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a050 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-981010-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
# t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a051 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-981039-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a052 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-984787-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
# t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
# t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
# t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servici1o
# t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
# t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a053 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-984899-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
# t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
# t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
# t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
# t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
# t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a054 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-985302-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a055 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-985552-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
# t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
# t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
# t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
# t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a056 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-987883-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a057 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-987955-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a058 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-987960-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
# t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
# t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
# t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
# t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
# t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a059 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-987971-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
# t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
# t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
# t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
# t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
# t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a060 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-987982-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
# t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
# t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
# t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
# t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
# t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a061 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-988009-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a062 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-988015-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a063 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-990917-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a064 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-991143-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a065 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-991166-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a066 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-991926-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a067 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-992777-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a068 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-1005728-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a069 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-1017497-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a070 =  Sheet1

#...
# document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-1018562-0-E F400.xlsx")

# Sheet1 = document.sheet_by_index(0)
# t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
# t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
# t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
# t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
# t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
# t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
# t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
# t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
# t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
# t013 = Sheet1.cell_value(86,0) #Código >> que significa
# t022 = Sheet1.cell_value(94,0) #Causal de la contratación
# t008 = Sheet1.cell_value(108,0) #Gestión
# t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
# t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
# t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
# t009 = Sheet1.cell_value(130,0) #Normativa utilizada
# t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
# t021 = Sheet1.cell_value(136,0) #Entidad
# t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
# t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
# t017 = Sheet1.cell_value(161,0) #Tipo de contratación
# t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
# t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
# t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
# t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
# t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
# t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
# t026 = Sheet1.cell_value(182,0) #Moneda del contrato
# t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
# t029 = Sheet1.cell_value(216,0) #Empresa
# t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
# t031 = Sheet1.cell_value(225,0) #Nro de contrato
# t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
# t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
# t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
# t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
# t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
# t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
# t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
# t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
# t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
# t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
# t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
# t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
# t044 = Sheet1.cell_value(295,0) #Precio unitario_A
# t045 = Sheet1.cell_value(305,0) #Precio unitario_B
# t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
# t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
# t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
# t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
# t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
# t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
# t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
# t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
# t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
# t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

# data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
#          t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
#          t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
#          t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
#          t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
#          t055)]

# Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
#                                    "Denominación de la Entidad", "Código proceso - CUCE", 
#                                     "Modalidad de contratación", 
#                                    "Número de documento/resolución que instruye la contratación", 
#                                    "Nro. de contratación en la gestión", 
#                                    "Fecha del documento/resolución que instruye la contratación", 
#                                    "Proyecto/Actividad", 
#                                    "Organismos Financiadores - Nombre del Organismo ", 
#                                    "Código >> que significa", "Causal de la contratación", 
#                                    "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
#                                    "Fecha de Informacón a la Contraloría", 
#                                    "Descripción categoria programatica", "Normativa utilizada", 
#                                    "Organismos Financiadores - % de Participación", 
#                                    "Entidad", "Dirección administrativa (SIGEP)", 
#                                    "Cargo de la autoridad que instruye la contratación", 
#                                    "Tipo de contratación", 
#                                    "Autoridad que instruye la contratación - Nombre y apellido", 
#                                    "Nacionalidad de la empresa", 
#                                    "Tipo documento_ Documento de identificación de la empresa", 
#                                    "Número de documento_ Documento de identificación de la empresa", 
#                                    "Nombre o razón social de la empresa", 
#                                    "Denominacion de la asociacion accidental", 
#                                    "Moneda del contrato", 
#                                    "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
#                                    "Nro de Certificado RUPE", "Nro de contrato", 
#                                    "Fecha de firma de contrato (día/mes/año)", 
#                                    "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
#                                    "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
#                                    "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
#                                    "Descripción del bien, obra, servicio general o de consultoría_A", 
#                                    "Descripción del bien, obra, servicio general o de consultoría_B", 
#                                    "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
#                                    "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
#                                    "La cantidad es fija_A", "La cantidad es fija_A", 
#                                    "Cantidad / Cantidad estimada si es variable_A", 
#                                    "Cantidad / Cantidad estimada si es variable_B", 
#                                    "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
#                                    "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
#                                    "Res. de Adjudicacion (nota)", 
#                                    "Contrato/Orden de Compra/Orden de Servicio", 
#                                    "Responsable_Res. de Adjudicacion", 
#                                    "Responsable_Contrato/Orden de Compra/Orden de Servicio"
# ])
a071 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-1023731-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a072 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-1024081-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a073 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-1024305-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a074 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-1025086-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a075 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-1025650-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a076 =  Sheet1

#...
document = xlrd.open_workbook("Form400_XLS_2019/19-0374-00-1028303-0-E F400.xlsx")

Sheet1 = document.sheet_by_index(0)
t001 = Sheet1.cell_value(20,0) #Código de la Entidad Pública
t002 = Sheet1.cell_value(32,0) #Denominación de la Entidad
t003 = Sheet1.cell_value(42,0) #Código proceso - CUCE
t004 = Sheet1.cell_value(46,0) #Modalidad de contratación
t019 = Sheet1.cell_value(51,0) #Número de documento/resolución que instruye la contratación
t005 = Sheet1.cell_value(71,0) #Nro. de contratación en la gestión
t006 = Sheet1.cell_value(76,0) #Fecha del documento/resolución que instruye la contratación
t011 = Sheet1.cell_value(82,0) #Proyecto/Actividad
t007 = Sheet1.cell_value(80,0) #Organismos Financiadores - Nombre del Organismo 
t013 = Sheet1.cell_value(86,0) #Código >> que significa
t022 = Sheet1.cell_value(94,0) #Causal de la contratación
t008 = Sheet1.cell_value(108,0) #Gestión
t018 = Sheet1.cell_value(112,0) #Objeto de la contratación >>> ojo AQUI SE MODIFICA
t020 = Sheet1.cell_value(117,0) #Fecha de Informacón a la Contraloría
t014 = Sheet1.cell_value(126,0) #Descripción categoria programatica
t009 = Sheet1.cell_value(130,0) #Normativa utilizada
t010 = Sheet1.cell_value(134,0) #Organismos Financiadores - % de Participación
t021 = Sheet1.cell_value(136,0) #Entidad
t012 = Sheet1.cell_value(139,0) #Dirección administrativa (SIGEP)
t016 = Sheet1.cell_value(157,0) #Cargo de la autoridad que instruye la contratación
t017 = Sheet1.cell_value(161,0) #Tipo de contratación
t015 = Sheet1.cell_value(231,0) #Autoridad que instruye la contratación - Nombre y apellido
t023 = Sheet1.cell_value(104,0) #Nacionalidad de la empresa
t024 = Sheet1.cell_value(165,0) #Tipo documento_ Documento de identificación de la empresa
t025 = Sheet1.cell_value(198,0) #Número de documento_ Documento de identificación de la empresa
t026 = Sheet1.cell_value(200,0) #Nombre o razón social de la empresa
t027 = Sheet1.cell_value(174,0) #Denominacion de la asociacion accidental
t026 = Sheet1.cell_value(182,0) #Moneda del contrato
t028 = Sheet1.cell_value(180,0) #Tipo de cambio (solo para moneda extranjera)
t029 = Sheet1.cell_value(216,0) #Empresa
t030 = Sheet1.cell_value(223,0) #Nro de Certificado RUPE
t031 = Sheet1.cell_value(225,0) #Nro de contrato
t032 = Sheet1.cell_value(227,0) #Fecha de firma de contrato (día/mes/año)
t033 = Sheet1.cell_value(229,0) #Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión
t034 = Sheet1.cell_value(231,0) #Nombre del responsable de firmar el contrato por la entidad pública
t035 = Sheet1.cell_value(233,0) #Fecha de recepción (Estimada)
t036 = Sheet1.cell_value(245,0) #Código del Catálogo (UNSPSC)
t037 = Sheet1.cell_value(279,0) #Partida presupuestaria
t038 = Sheet1.cell_value(281,0) #Descripción del bien, obra, servicio general o de consultoría_A
t039 = Sheet1.cell_value(299,0) #Descripción del bien, obra, servicio general o de consultoría_B
t040 = Sheet1.cell_value(285,0) #Nro. de contrato_A
t041 = Sheet1.cell_value(301,0) #Nro. de contrato_B
t042 = Sheet1.cell_value(287,0) #Unidad de medida_A
t043 = Sheet1.cell_value(303,0) #Unidad de medida_B
t044 = Sheet1.cell_value(295,0) #Precio unitario_A
t045 = Sheet1.cell_value(305,0) #Precio unitario_B
t046 = Sheet1.cell_value(293,0) #La cantidad es fija_A
t047 = Sheet1.cell_value(326,0) #La cantidad es fija_B
t048 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_A
t049 = Sheet1.cell_value(293,0) #Cantidad / Cantidad estimada si es variable_B
t050 = Sheet1.cell_value(295,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t051 = Sheet1.cell_value(305,0) #Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A
t052 = Sheet1.cell_value(330,0) #Res. de Adjudicacion (nota)
t053 = Sheet1.cell_value(328,0) #Contrato/Orden de Compra/Orden de Servicio
t054 = Sheet1.cell_value(332,0) #Responsable_Res. de Adjudicacion
t055 = Sheet1.cell_value(340,0) #Responsable_Contrato/Orden de Compra/Orden de Servicio

data = [(t001, t002, t003, t004, t019, t005, t006, t011, t007, t013, t022, 
         t008, t018, t020, t014, t009, t010, t021, t012, t016, t017, t015, 
         t023, t024, t025, t026, t027, t026, t028, t029, t030, t031, t032, 
         t033, t034, t035, t036, t037, t038, t039, t040, t041, t042, t043, 
         t044, t045, t046, t047, t048, t049, t050, t051, t052, t053, t054, 
         t055)]

Sheet1 = pd.DataFrame(data, columns=["Código de la Entidad Pública", 
                                   "Denominación de la Entidad", "Código proceso - CUCE", 
                                   "Modalidad de contratación", 
                                   "Número de documento/resolución que instruye la contratación", 
                                   "Nro. de contratación en la gestión", 
                                   "Fecha del documento/resolución que instruye la contratación", 
                                   "Proyecto/Actividad", 
                                   "Organismos Financiadores - Nombre del Organismo ", 
                                   "Código >> que significa", "Causal de la contratación", 
                                   "Gestión", "Objeto de la contratación >>> ojo AQUI SE MODIFICA", 
                                   "Fecha de Informacón a la Contraloría", 
                                   "Descripción categoria programatica", "Normativa utilizada", 
                                   "Organismos Financiadores - % de Participación", 
                                   "Entidad", "Dirección administrativa (SIGEP)", 
                                   "Cargo de la autoridad que instruye la contratación", 
                                   "Tipo de contratación", 
                                   "Autoridad que instruye la contratación - Nombre y apellido", 
                                   "Nacionalidad de la empresa", 
                                   "Tipo documento_ Documento de identificación de la empresa", 
                                   "Número de documento_ Documento de identificación de la empresa", 
                                   "Nombre o razón social de la empresa", 
                                   "Denominacion de la asociacion accidental", 
                                   "Moneda del contrato", 
                                   "Tipo de cambio (solo para moneda extranjera)", "Empresa", 
                                   "Nro de Certificado RUPE", "Nro de contrato", 
                                   "Fecha de firma de contrato (día/mes/año)", 
                                   "Monto del contrato/ Monto estimado para cantidades variables/Monto de inversión para concesión", 
                                   "Nombre del responsable de firmar el contrato por la entidad pública", "Fecha de recepción (Estimada)", 
                                   "Código del Catálogo (UNSPSC)", "Partida presupuestaria", 
                                   "Descripción del bien, obra, servicio general o de consultoría_A", 
                                   "Descripción del bien, obra, servicio general o de consultoría_B", 
                                   "Nro. de contrato_A", "Nro. de contrato_B", "Unidad de medida_A", 
                                   "Unidad de medida_B", "Precio unitario_A", "Precio unitario_B", 
                                   "La cantidad es fija_A", "La cantidad es fija_A", 
                                   "Cantidad / Cantidad estimada si es variable_A", 
                                   "Cantidad / Cantidad estimada si es variable_B", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Monto total (p.unit. x cantidad) / Total estimado cuando la cantidad es variable_A", 
                                   "Res. de Adjudicacion (nota)", 
                                   "Contrato/Orden de Compra/Orden de Servicio", 
                                   "Responsable_Res. de Adjudicacion", 
                                   "Responsable_Contrato/Orden de Compra/Orden de Servicio"
])
a077 =  Sheet1

#...

pd.concat([a001, a002, a003, a004, a005, a006, a007, a008, a009, a010, a011, a012, a013, a014, 
           a015, a016, a017, a018, a019, a020, a021, a022, a023, a024, a025, a026, a027, a028, 
           a029, a030, a031, a032, a033, a034, a035, a036, a037, a038, a039, a040, a041, a042, 
           a043, a044, a045, a046, a047, a048, a049, a050, a051, a052, a053, a054, a055, a056, 
           a057, a058, a059, a060, a061, a062, a063, a064, a065, a066, a067, a068, a069, a070, 
           a071, a072, a073, a074, a075, a076, a077]).to_csv("dat001.csv")



