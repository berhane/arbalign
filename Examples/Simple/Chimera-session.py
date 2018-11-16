import cPickle, base64
try:
	from SimpleSession.versions.v65 import beginRestore,\
	    registerAfterModelsCB, reportRestoreError, checkVersion
except ImportError:
	from chimera import UserError
	raise UserError('Cannot open session that was saved in a'
	    ' newer version of Chimera; update your version')
checkVersion([1, 13, 1, 41920])
import chimera
from chimera import replyobj
replyobj.status('Restoring session...', \
    blankAfter=0)
replyobj.status('Beginning session restore...', \
    blankAfter=0, secondary=True)
beginRestore()

def restoreCoreModels():
	from SimpleSession.versions.v65 import init, restoreViewer, \
	     restoreMolecules, restoreColors, restoreSurfaces, \
	     restoreVRML, restorePseudoBondGroups, restoreModelAssociations
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwROfYdVCWJhbGxTY2FsZXEDSwRHP8mZmaAAAAB9h1UJcG9pbnRTaXplcQRLBEc/8AAAAAAAAH2HVQVjb2xvcnEFSwRLAH1xBihLAV1xB0sBYUsCXXEISwJhSwNdcQlLA2F1h1UKcmliYm9uVHlwZXEKSwRLAH2HVQpzdGlja1NjYWxlcQtLBEc/4AAAAAAAAH2HVQxtbUNJRkhlYWRlcnNxDF1xDShOTk5OZVUMYXJvbWF0aWNNb2RlcQ5LBEsBfYdVCnZkd0RlbnNpdHlxD0sER0AUAAAAAAAAfYdVBmhpZGRlbnEQSwSJfYdVDWFyb21hdGljQ29sb3JxEUsETn2HVQ9yaWJib25TbW9vdGhpbmdxEksESwB9h1UJYXV0b2NoYWlucRNLBIh9h1UKcGRiVmVyc2lvbnEUSwRLAH2HVQhvcHRpb25hbHEVfXEWVQhvcGVuZWRBc3EXiIlLBChVPy9Vc2Vycy90ZW1lbHNvYi9EZXNrdG9wL2RldmVsb3BtZW50L2FyYmFsaWduL0V4YW1wbGVzL01vbC1BLnh5enEYTk5LAXRxGX1xGigoVVAvVXNlcnMvdGVtZWxzb2IvRGVza3RvcC9kZXZlbG9wbWVudC9hcmJhbGlnbi9FeGFtcGxlcy9Nb2wtQi1hbGlnbmVkX3RvLU1vbC1BLnh5enEbTk5LAXRxHF1xHUsDYShVPy9Vc2Vycy90ZW1lbHNvYi9EZXNrdG9wL2RldmVsb3BtZW50L2FyYmFsaWduL0V4YW1wbGVzL01vbC1CLnh5enEeTk5LAXRxH11xIEsBYXWHh3NVD2xvd2VyQ2FzZUNoYWluc3EhSwSJfYdVCWxpbmVXaWR0aHEiSwRHP/AAAAAAAAB9h1UPcmVzaWR1ZUxhYmVsUG9zcSNLBEsAfYdVBG5hbWVxJEsEWA8AAABNb2xfQSA9IEZHRy0yNTJ9cSUoWBoAAABNb2wtQi1hbGlnbmVkX3RvLU1vbC1BLnh5el1xJksDYVgPAAAATW9sX0IgPSBGR0ctMjU3XXEnSwFhdYdVD2Fyb21hdGljRGlzcGxheXEoSwSJfYdVD3JpYmJvblN0aWZmbmVzc3EpSwRHP+mZmZmZmZp9h1UKcGRiSGVhZGVyc3EqXXErKH1xLH1xLX1xLn1xL2VVA2lkc3EwSwRLA0sAhn1xMShLAksAhl1xMksCYUsBSwCGXXEzSwFhSwBLAIZdcTRLAGF1h1UOc3VyZmFjZU9wYWNpdHlxNUsER7/wAAAAAAAAfYdVEGFyb21hdGljTGluZVR5cGVxNksESwJ9h1UUcmliYm9uSGlkZXNNYWluY2hhaW5xN0sEiH2HVQdkaXNwbGF5cThLBIh9h3Uu'))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksEVQEgfYdVC2ZpbGxEaXNwbGF5cQNLBIl9h1UEbmFtZXEESwRYAwAAAFVOS32HVQVjaGFpbnEFSwRYAQAAACB9h1UOcmliYm9uRHJhd01vZGVxBksESwJ9h1UCc3NxB0sEiYmGfYdVCG1vbGVjdWxlcQhLBEsAfXEJKEsBTl1xCksBSwGGcQthhksCTl1xDEsCSwGGcQ1hhksDTl1xDksDSwGGcQ9hhnWHVQtyaWJib25Db2xvcnEQSwROfYdVBWxhYmVscRFLBFgAAAAAfYdVCmxhYmVsQ29sb3JxEksETn2HVQhmaWxsTW9kZXETSwRLAX2HVQVpc0hldHEUSwSJfYdVC2xhYmVsT2Zmc2V0cRVLBE59h1UIcG9zaXRpb25xFl1xFyhLAUsBhnEYSwFLAYZxGUsBSwGGcRpLAUsBhnEbZVUNcmliYm9uRGlzcGxheXEcSwSJfYdVCG9wdGlvbmFscR19VQRzc0lkcR5LBEr/////fYd1Lg=='))
	atomInfo = cPickle.loads(base64.b64decode('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'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVjb2xvcnECS5ROfYdVBWF0b21zcQNdcQQoXXEFKEsISwllXXEGKEsJSwplXXEHKEsJSwxlXXEIKEsKSwtlXXEJKEsMSw1lXXEKKEsMSw5lXXELKEsMSw9lXXEMKEsPSxBlXXENKEsPSxFlXXEOKEsRSxJlXXEPKEsRSxNlXXEQKEsTSxRlXXERKEsTSxVlXXESKEsTSxZlXXETKEsWSxdlXXEUKEsWSxhlXXEVKEsYSxllXXEWKEsYSxplXXEXKEsaSxtlXXEYKEsaSx5lXXEZKEsaSx9lXXEaKEsbSxxlXXEbKEsbSx1lXXEcKEsfSyBlXXEdKEsfSyFlXXEeKEsfSyJlXXEfKEsiSyNlXXEgKEsiSytlXXEhKEsjSyRlXXEiKEsjSyVlXXEjKEslSyZlXXEkKEslSydlXXElKEsnSyhlXXEmKEsnSyllXXEnKEspSyplXXEoKEspSytlXXEpKEsrSyxlXXEqKEstSy9lXXErKEstS0BlXXEsKEstS0JlXXEtKEstS0xlXXEuKEsuSzJlXXEvKEsuSzNlXXEwKEsuSzxlXXExKEsvS0tlXXEyKEsvS05lXXEzKEswSzFlXXE0KEswSz1lXXE1KEswSz9lXXE2KEswS0tlXXE3KEsxS09lXXE4KEsxS1BlXXE5KEsySzRlXXE6KEsySzplXXE7KEszSzZlXXE8KEszS0FlXXE9KEs0SzdlXXE+KEs0S0RlXXE/KEs1SzllXXFAKEs1S0xlXXFBKEs1S1FlXXFCKEs2SzdlXXFDKEs2SzhlXXFEKEs3S0ZlXXFFKEs4SzllXXFGKEs4S0VlXXFHKEs4S0hlXXFIKEs5S0dlXXFJKEs5S01lXXFKKEs7S0tlXXFLKEs+S09lXXFMKEtDS0xlXXFNKEtJS01lXXFOKEtKS01lXXFPKEtSS1NlXXFQKEtTS1RlXXFRKEtTS1ZlXXFSKEtUS1VlXXFTKEtWS1dlXXFUKEtWS1hlXXFVKEtWS1llXXFWKEtZS1plXXFXKEtZS1tlXXFYKEtbS1xlXXFZKEtbS11lXXFaKEtdS15lXXFbKEtdS19lXXFcKEtdS2BlXXFdKEtgS2FlXXFeKEtgS2JlXXFfKEtiS2NlXXFgKEtiS2RlXXFhKEtkS2VlXXFiKEtkS2hlXXFjKEtkS2llXXFkKEtlS2ZlXXFlKEtlS2dlXXFmKEtpS2plXXFnKEtpS2tlXXFoKEtpS2xlXXFpKEtsS21lXXFqKEtsS3VlXXFrKEttS25lXXFsKEttS29lXXFtKEtvS3BlXXFuKEtvS3FlXXFvKEtxS3JlXXFwKEtxS3NlXXFxKEtzS3RlXXFyKEtzS3VlXXFzKEt1S3ZlXXF0KEt3S3hlXXF1KEt4S3llXXF2KEt4S3tlXXF3KEt5S3plXXF4KEt7S3xlXXF5KEt7S31lXXF6KEt7S35lXXF7KEt+S39lXXF8KEt+S4BlXXF9KEuAS4FlXXF+KEuAS4JlXXF/KEuCS4NlXXGAKEuCS4RlXXGBKEuCS4VlXXGCKEuFS4ZlXXGDKEuFS4dlXXGEKEuHS4hlXXGFKEuHS4llXXGGKEuJS4plXXGHKEuJS4tlXXGIKEuJS45lXXGJKEuKS4xlXXGKKEuKS41lXXGLKEuOS49lXXGMKEuOS5BlXXGNKEuOS5FlXXGOKEuRS5JlXXGPKEuRS5plXXGQKEuSS5NlXXGRKEuSS5RlXXGSKEuUS5VlXXGTKEuUS5ZlXXGUKEuWS5dlXXGVKEuWS5hlXXGWKEuYS5llXXGXKEuYS5plXXGYKEuaS5tlZVUFbGFiZWxxmUuUWAAAAAB9h1UIaGFsZmJvbmRxmkuUiH2HVQZyYWRpdXNxm0uURz/JmZmgAAAAfYdVC2xhYmVsT2Zmc2V0cZxLlE59h1UIZHJhd01vZGVxnUuUSwF9h1UIb3B0aW9uYWxxnn1VB2Rpc3BsYXlxn0uUSwJ9h3Uu'))
	crdInfo = cPickle.loads(base64.b64decode('gAJ9cQEoSwB9cQIoSwBdcQMoR8AIhR64UeuFRz+987ZFocrBR8ACnbItDlYEh3EER8AIO2RaHKwIR7+gYk3S8an8R7/yEGJN0vGqh3EFR8AJPXCj1wo9Rz/vvnbItDlYR7/RiTdLxqfwh3EGR8AH64UeuFHsRz/lDlYEGJN1Rz/ki0OVgQYlh3EHR8AGxJul41P4R7/2VgQYk3S8R7/eBBiTdLxqh3EIR8AG1wo9cKPXR8ABLQ5WBBiTR7/0BBiTdLxqh3EJR8ANan752yLRR7/5LxqfvnbJRz/LxqfvnbIth3EKR7/5hR64UeuFR7/4HKwIMSbpRz/QtDlYEGJOh3ELR7/rItDlYEGJR8AA41P3ztkXR7+ybpeNT987h3EMR7/2bpeNT987R7/seuFHrhR7Rz/2/fO2RaHLh3ENR8AB1P3ztkWiR7+/O2RaHKwIRz//Jul41P30h3EOR7+1wo9cKPXDR7/zgQYk3S8bR0ABBiTdLxqgh3EPR7+keuFHrhR7R8ACVgQYk3S8R0AChR64UeuFh3EQR7+zMzMzMzMzR7/l87ZFocrBR0AIlYEGJN0vh3ERRz/xcKPXCj1xR7/rCj1wo9cKRz/10vGp++dth3ESRz/3peNT987ZRz+z987ZFocrRz/341P3ztkXh3ETRz/4Yk3S8an8R7/5LxqfvnbJRz/T52yLQ5WBh3EURz/udsi0OVgQR8AE1wo9cKPXR7+uNT987ZFoh3EVR0AGDEm6XjU/R7/wxJul41P4R7/a4UeuFHrhh3EWR0AL2yLQ5WBCR8AAul41P3zuR7/x987ZFocrh3EXR0AGdLxqfvnbR8AFDEm6XjU/R7/6euFHrhR7h3EYR0AO52yLQ5WBR8AF987ZFocrR7/czMzMzMzNh3EZR0ALbpeNT987R7/iwIMSbpeNRz/ThR64UeuFh3EaR0ACkWhysCDFRz+g5WBBiTdMR7/21P3ztkWih3EbR0AJwo9cKPXDRz/VHrhR64UfR7//fO2RaHKwh3EcRz/6JN0vGp++R7/awIMSbpeNR8ABLQ5WBBiTh3EdRz/6zMzMzMzNRz/zU/fO2RaHR7/oEGJN0vGqh3EeR0ADdsi0OVgQR0AAN0vGp++eRz+4EGJN0vGqh3EfR0AMAAAAAAAARz/9vnbItDlYRz/HbItDlYEGh3EgRz/9WBBiTdLyR0AIeNT987ZGRz/qFHrhR64Uh3EhR0ADeuFHrhR7R0ANdsi0OVgQRz/3aHKwIMSch3EiRz/dwo9cKPXDR0AKU/fO2RaHRz/mFHrhR64Uh3EjR79ok3S8an76R0AQXS8an753Rz/z87ZFocrBh3EkR7/TAgxJul41R0AD/fO2RaHLR7/FgQYk3S8bh3ElR7/1tkWhysCDR0AFYk3S8an8R7/SHKwIMSbph3EmRz/TpeNT987ZRz/3ZFocrAgxR7/sIMSbpeNUh3EnR7/SsCDEm6XjRz/rKwIMSbpeR7/4sCDEm6Xjh3EoZVUGYWN0aXZlcSlLAHVLAX1xKihLAF1xKyhHP2BiTdLxqfxHQAHnbItDlYFHv/VP3ztkWh2HcSxHP9qfvnbItDlHwAKl41P3ztlHP8YEGJN0vGqHcS1HP/VcKPXCj1xHP/mZmZmZmZpHv+7ZFocrAgyHcS5HQAbMzMzMzM1HP/CbpeNT989HP+udsi0OVgSHcS9HQAjztkWhysFHv9ysCDEm6XlHP+T1wo9cKPaHcTBHv7S8an752yNHwAfU/fO2RaJHv+6fvnbItDmHcTFHv9rhR64UeuFHv/gQYk3S8apHP+141P3ztkaHcTJHv/asCDEm6XlHwAaHKwIMSbpHv/UWhysCDEqHcTNHv/lLxqfvnbJHP/nztkWhysFHP9wYk3S8an+HcTRHv/w1P3ztkWhHv/U7ZFocrAhHP+ItDlYEGJOHcTVHwAIEGJN0vGpHwAAEGJN0vGpHv+HKwIMSbpiHcTZHwAUk3S8an75Hv9rxqfvnbItHP/YYk3S8an+HcTdHwAdHrhR64UhHP+5WBBiTdLxHP+dcKPXCj1yHcThHP+ItDlYEGJNHwAztkWhysCFHv/isCDEm6XmHcTlHP+oEGJN0vGpHP/wYk3S8an9HP+9T987ZFoeHcTpHP/cWhysCDEpHwAPItDlYEGJHP95WBBiTdLyHcTtHQAcAAAAAAABHP/O6XjU/fO5HP/7dLxqfvneHcTxHQAe0OVgQYk5Hv7ItDlYEGJNHv/MzMzMzMzOHcT1HQA0an752yLRHP/nGp++dsi1HP9euFHrhR66HcT5Hv4BiTdLxqfxHQAoMSbpeNT9Hv+4MSbpeNT+HcT9Hv564UeuFHrhHv/AcrAgxJulHP/zQ5WBBiTeHcUBHv6aHKwIMSbpHQAIvGp++dslHwANR64UeuFKHcUFHv/wUeuFHrhRHP+/3ztkWhytHv/dHrhR64UiHcUJHv/0CDEm6XjVHwAqj1wo9cKRHwAF41P3ztkaHcUNHwAF0vGp++dtHv841P3ztkWhHQALQ5WBBiTeHcURHwApWBBiTdLxHv/5aHKwIMSdHv+q4UeuFHriHcUVHwAso9cKPXClHP/lDlYEGJN1HP/euFHrhR66HcUZHwAzlYEGJN0xHv+yLQ5WBBiVHP/kSbpeNT9+HcUdHwBBFocrAgxJHP/rxqfvnbItHv+kOVgQYk3WHcUhHwBHocrAgxJxHP8dLxqfvnbJHv9TMzMzMzM2HcUlHP/j52yLQ5WBHP/d0vGp++dtHP9ZWBBiTdLyHcUpHv/KsCDEm6XlHP/isCDEm6XlHv+rItDlYEGKHcUtHwA141P3ztkZHP+k/fO2RaHNHv9/vnbItDlaHcUxHQAE9cKPXCj1HP/RysCDEm6ZHv/1gQYk3S8eHcU1HQAmJN0vGp/BHv+rZFocrAgxHv+PXCj1wo9eHcU5HQAoeuFHrhR9Hv/OBBiTdLxtHP/k3S8an756HcU9Hv+4EGJN0vGpHQAF0vGp++dtHP/VcKPXCj1yHcVBlaClLAHVLAn1xUShLAF1xUihHwAiFHrhR64VHP73ztkWhysFHwAKdsi0OVgSHcVNHwAg7ZFocrAhHv6BiTdLxqfxHv/IQYk3S8aqHcVRHwAk9cKPXCj1HP+++dsi0OVhHv9GJN0vGp/CHcVVHwAfrhR64UexHP+UOVgQYk3VHP+SLQ5WBBiWHcVZHwAbEm6XjU/hHv/ZWBBiTdLxHv94EGJN0vGqHcVdHwAbXCj1wo9dHwAEtDlYEGJNHv/QEGJN0vGqHcVhHwA1qfvnbItFHv/kvGp++dslHP8vGp++dsi2HcVlHv/mFHrhR64VHv/gcrAgxJulHP9C0OVgQYk6HcVpHv+si0OVgQYlHwADjU/fO2RdHv7Jul41P3zuHcVtHv/Zul41P3ztHv+x64UeuFHtHP/b987ZFocuHcVxHwAHU/fO2RaJHv787ZFocrAhHP/8m6XjU/fSHcV1Hv7XCj1wo9cNHv/OBBiTdLxtHQAEGJN0vGqCHcV5Hv6R64UeuFHtHwAJWBBiTdLxHQAKFHrhR64WHcV9Hv7MzMzMzMzNHv+XztkWhysFHQAiVgQYk3S+HcWBHP/Fwo9cKPXFHv+sKPXCj1wpHP/XS8an7522HcWFHP/el41P3ztlHP7P3ztkWhytHP/fjU/fO2ReHcWJHP/hiTdLxqfxHv/kvGp++dslHP9PnbItDlYGHcWNHP+52yLQ5WBBHwATXCj1wo9dHv641P3ztkWiHcWRHQAYMSbpeNT9Hv/DEm6XjU/hHv9rhR64UeuGHcWVHQAvbItDlYEJHwAC6XjU/fO5Hv/H3ztkWhyuHcWZHQAZ0vGp++dtHwAUMSbpeNT9Hv/p64UeuFHuHcWdHQA7nbItDlYFHwAX3ztkWhytHv9zMzMzMzM2HcWhHQAtul41P3ztHv+LAgxJul41HP9OFHrhR64WHcWlHQAKRaHKwIMVHP6DlYEGJN0xHv/bU/fO2RaKHcWpHQAnCj1wo9cNHP9UeuFHrhR9Hv/987ZFocrCHcWtHP/ok3S8an75Hv9rAgxJul41HwAEtDlYEGJOHcWxHP/rMzMzMzM1HP/NT987ZFodHv+gQYk3S8aqHcW1HQAN2yLQ5WBBHQAA3S8an755HP7gQYk3S8aqHcW5HQAwAAAAAAABHP/2+dsi0OVhHP8dsi0OVgQaHcW9HP/1YEGJN0vJHQAh41P3ztkZHP+oUeuFHrhSHcXBHQAN64UeuFHtHQA12yLQ5WBBHP/docrAgxJyHcXFHP93Cj1wo9cNHQApT987ZFodHP+YUeuFHrhSHcXJHv2iTdLxqfvpHQBBdLxqfvndHP/PztkWhysGHcXNHv9MCDEm6XjVHQAP987ZFoctHv8WBBiTdLxuHcXRHv/W2RaHKwINHQAViTdLxqfxHv9IcrAgxJumHcXVHP9Ol41P3ztlHP/dkWhysCDFHv+wgxJul41SHcXZHv9KwIMSbpeNHP+srAgxJul5Hv/iwIMSbpeOHcXdlaClLAHVLA31xeChLAF1xeShHwAoeuFHrhR9HP/OBBiTdLxtHv/k3S8an756HcXpHwAjztkWhysFHP9ysCDEm6XlHv+T1wo9cKPaHcXtHwAmJN0vGp/BHP+rZFocrAgxHP+PXCj1wo9eHcXxHwAe0OVgQYk5HP7ItDlYEGJNHP/MzMzMzMzOHcX1HwAbMzMzMzM1Hv/CbpeNT989Hv+udsi0OVgSHcX5HwAcAAAAAAABHv/O6XjU/fO5Hv/7dLxqfvneHcX9HwA0an752yLRHv/nGp++dsi1Hv9euFHrhR66HcYBHv/j52yLQ5WBHv/d0vGp++dtHv9ZWBBiTdLyHcYFHv+oEGJN0vGpHv/wYk3S8an9Hv+9T987ZFoeHcYJHv/VcKPXCj1xHv/mZmZmZmZpHP+7ZFocrAgyHcYNHwAE9cKPXCj1Hv/RysCDEm6ZHP/1gQYk3S8eHcYRHv2BiTdLxqfxHwAHnbItDlYFHP/VP3ztkWh2HcYVHP4BiTdLxqfxHwAoMSbpeNT9HP+4MSbpeNT+HcYZHP6aHKwIMSbpHwAIvGp++dslHQANR64UeuFKHcYdHP/KsCDEm6XlHv/isCDEm6XlHP+rItDlYEGKHcYhHP/wUeuFHrhRHv+/3ztkWhytHP/dHrhR64UiHcYlHP/lLxqfvnbJHv/nztkWhysFHv9wYk3S8an+HcYpHP+4EGJN0vGpHwAF0vGp++dtHv/VcKPXCj1yHcYtHQAdHrhR64UhHv+5WBBiTdLxHv+dcKPXCj1yHcYxHQA141P3ztkZHv+k/fO2RaHNHP9/vnbItDlaHcY1HQAso9cKPXClHv/lDlYEGJN1Hv/euFHrhR66HcY5HQBBFocrAgxJHv/rxqfvnbItHP+kOVgQYk3WHcY9HQBHocrAgxJxHv8dLxqfvnbJHP9TMzMzMzM2HcZBHQAUk3S8an75HP9rxqfvnbItHv/YYk3S8an+HcZFHQAzlYEGJN0xHP+yLQ5WBBiVHv/kSbpeNT9+HcZJHQAF0vGp++dtHP841P3ztkWhHwALQ5WBBiTeHcZNHP/w1P3ztkWhHP/U7ZFocrAhHv+ItDlYEGJOHcZRHQAIEGJN0vGpHQAAEGJN0vGpHP+HKwIMSbpiHcZVHQApWBBiTdLxHP/5aHKwIMSdHP+q4UeuFHriHcZZHP/asCDEm6XlHQAaHKwIMSbpHP/UWhysCDEqHcZdHP/0CDEm6XjVHQAqj1wo9cKRHQAF41P3ztkaHcZhHP7S8an752yNHQAfU/fO2RaJHP+6fvnbItDmHcZlHv+ItDlYEGJNHQAztkWhysCFHP/isCDEm6XmHcZpHv9qfvnbItDlHQAKl41P3ztlHv8YEGJN0vGqHcZtHv/cWhysCDEpHQAPItDlYEGJHv95WBBiTdLyHcZxHP9rhR64UeuFHP/gQYk3S8apHv+141P3ztkaHcZ1HP564UeuFHrhHP/AcrAgxJulHv/zQ5WBBiTeHcZ5laClLAHV1Lg=='))
	surfInfo = {'category': (0, None, {}), 'probeRadius': (0, None, {}), 'pointSize': (0, None, {}), 'name': [], 'density': (0, None, {}), 'colorMode': (0, None, {}), 'useLighting': (0, None, {}), 'transparencyBlendMode': (0, None, {}), 'molecule': [], 'smoothLines': (0, None, {}), 'lineWidth': (0, None, {}), 'allComponents': (0, None, {}), 'twoSidedLighting': (0, None, {}), 'customVisibility': [], 'drawMode': (0, None, {}), 'display': (0, None, {}), 'customColors': []}
	vrmlInfo = {'subid': (0, None, {}), 'display': (0, None, {}), 'id': (0, None, {}), 'vrmlString': [], 'name': (0, None, {})}
	colors = {u'Ru': ((0.141176, 0.560784, 0.560784), 1, u'default'), u'Re': ((0.14902, 0.490196, 0.670588), 1, u'default'), u'Rf': ((0.8, 0, 0.34902), 1, u'default'), u'Ra': ((0, 0.490196, 0), 1, u'default'), u'Rb': ((0.439216, 0.180392, 0.690196), 1, u'default'), u'Rn': ((0.258824, 0.509804, 0.588235), 1, u'default'), u'Rh': ((0.0392157, 0.490196, 0.54902), 1, u'default'), u'Be': ((0.760784, 1, 0), 1, u'default'), u'Ba': ((0, 0.788235, 0), 1, u'default'), u'Bh': ((0.878431, 0, 0.219608), 1, u'default'), u'Bi': ((0.619608, 0.309804, 0.709804), 1, u'default'), u'Bk': ((0.541176, 0.309804, 0.890196), 1, u'default'), u'Br': ((0.65098, 0.160784, 0.160784), 1, u'default'), u'H': ((1, 1, 1), 1, u'default'), u'P': ((1, 0.501961, 0), 1, u'default'), u'Os': ((0.14902, 0.4, 0.588235), 1, u'default'), u'Es': ((0.701961, 0.121569, 0.831373), 1, u'default'), u'Hg': ((0.721569, 0.721569, 0.815686), 1, u'default'), u'Ge': ((0.4, 0.560784, 0.560784), 1, u'default'), u'Gd': ((0.270588, 1, 0.780392), 1, u'default'), u'Ga': ((0.760784, 0.560784, 0.560784), 1, u'default'), u'Pr': ((0.85098, 1, 0.780392), 1, u'default'),
u'Pt': ((0.815686, 0.815686, 0.878431), 1, u'default'), u'Pu': ((0, 0.419608, 1), 1, u'default'), u'C': ((0.564706, 0.564706, 0.564706), 1, u'default'), u'Pb': ((0.341176, 0.34902, 0.380392), 1, u'default'), u'Pa': ((0, 0.631373, 1), 1, u'default'), u'Pd': ((0, 0.411765, 0.521569), 1, u'default'), u'Cd': ((1, 0.85098, 0.560784), 1, u'default'), u'Po': ((0.670588, 0.360784, 0), 1, u'default'), u'Pm': ((0.639216, 1, 0.780392), 1, u'default'), u'Hs': ((0.901961, 0, 0.180392), 1, u'default'), u'Ho': ((0, 1, 0.611765), 1, u'default'), u'Hf': ((0.301961, 0.760784, 1), 1, u'default'), u'Mo': ((0.329412, 0.709804, 0.709804), 1, u'default'), u'He': ((0.85098, 1, 1), 1, u'default'), u'Md': ((0.701961, 0.0509804, 0.65098), 1, u'default'), u'Mg': ((0.541176, 1, 0), 1, u'default'), u'K': ((0.560784, 0.25098, 0.831373), 1, u'default'), u'Mn': ((0.611765, 0.478431, 0.780392), 1, u'default'), u'O': ((1, 0.0509804, 0.0509804), 1, u'default'), u'Mt': ((0.921569, 0, 0.14902), 1, u'default'), u'S': ((1, 1, 0.188235), 1, u'default'), u'W': ((0.129412, 0.580392, 0.839216), 1, u'default'),
u'sky blue': ((0.529412, 0.807843, 0.921569), 1, u'default'), u'Zn': ((0.490196, 0.501961, 0.690196), 1, u'default'), u'plum': ((0.866667, 0.627451, 0.866667), 1, u'default'), u'Eu': ((0.380392, 1, 0.780392), 1, u'default'), u'Zr': ((0.580392, 0.878431, 0.878431), 1, u'default'), u'Er': ((0, 0.901961, 0.458824), 1, u'default'), u'Ni': ((0.313725, 0.815686, 0.313725), 1, u'default'), u'No': ((0.741176, 0.0509804, 0.529412), 1, u'default'), u'Na': ((0.670588, 0.360784, 0.94902), 1, u'default'), u'Nb': ((0.45098, 0.760784, 0.788235), 1, u'default'), u'Nd': ((0.780392, 1, 0.780392), 1, u'default'), u'Ne': ((0.701961, 0.890196, 0.960784), 1, u'default'), u'Np': ((0, 0.501961, 1), 1, u'default'), u'Fr': ((0.258824, 0, 0.4), 1, u'default'), u'Fe': ((0.878431, 0.4, 0.2), 1, u'default'), u'Fm': ((0.701961, 0.121569, 0.729412), 1, u'default'), u'B': ((1, 0.709804, 0.709804), 1, u'default'), u'F': ((0.564706, 0.878431, 0.313725), 1, u'default'), u'Sr': ((0, 1, 0), 1, u'default'), u'N': ((0.188235, 0.313725, 0.972549), 1, u'default'), u'Kr': ((0.360784, 0.721569, 0.819608), 1, u'default'),
u'Si': ((0.941176, 0.784314, 0.627451), 1, u'default'), u'Sn': ((0.4, 0.501961, 0.501961), 1, u'default'), u'Sm': ((0.560784, 1, 0.780392), 1, u'default'), u'V': ((0.65098, 0.65098, 0.670588), 1, u'default'), u'Sc': ((0.901961, 0.901961, 0.901961), 1, u'default'), u'Sb': ((0.619608, 0.388235, 0.709804), 1, u'default'), u'Sg': ((0.85098, 0, 0.270588), 1, u'default'), u'Se': ((1, 0.631373, 0), 1, u'default'), u'Co': ((0.941176, 0.564706, 0.627451), 1, u'default'), u'Cm': ((0.470588, 0.360784, 0.890196), 1, u'default'), u'Cl': ((0.121569, 0.941176, 0.121569), 1, u'default'), u'Ca': ((0.239216, 1, 0), 1, u'default'), u'Cf': ((0.631373, 0.211765, 0.831373), 1, u'default'), u'Ce': ((1, 1, 0.780392), 1, u'default'), u'Xe': ((0.258824, 0.619608, 0.690196), 1, u'default'), u'Lu': ((0, 0.670588, 0.141176), 1, u'default'), u'light green': ((0.564706, 0.933333, 0.564706), 1, u'default'), u'Cs': ((0.341176, 0.0901961, 0.560784), 1, u'default'), u'Cr': ((0.541176, 0.6, 0.780392), 1, u'default'), u'Cu': ((0.784314, 0.501961, 0.2), 1, u'default'), u'La': ((0.439216, 0.831373, 1), 1, u'default'),
u'Li': ((0.8, 0.501961, 1), 1, u'default'), u'Tl': ((0.65098, 0.329412, 0.301961), 1, u'default'), u'Tm': ((0, 0.831373, 0.321569), 1, u'default'), u'Lr': ((0.780392, 0, 0.4), 1, u'default'), u'Th': ((0, 0.729412, 1), 1, u'default'), u'Ti': ((0.74902, 0.760784, 0.780392), 1, u'default'), u'tan': ((0.823529, 0.705882, 0.54902), 1, u'default'), u'Te': ((0.831373, 0.478431, 0), 1, u'default'), u'Tb': ((0.188235, 1, 0.780392), 1, u'default'), u'Tc': ((0.231373, 0.619608, 0.619608), 1, u'default'), u'Ta': ((0.301961, 0.65098, 1), 1, u'default'), u'Yb': ((0, 0.74902, 0.219608), 1, u'default'), u'Db': ((0.819608, 0, 0.309804), 1, u'default'), u'Dy': ((0.121569, 1, 0.780392), 1, u'default'), u'I': ((0.580392, 0, 0.580392), 1, u'default'), u'U': ((0, 0.560784, 1), 1, u'default'), u'Y': ((0.580392, 1, 1), 1, u'default'), u'Ac': ((0.439216, 0.670588, 0.980392), 1, u'default'), u'Ag': ((0.752941, 0.752941, 0.752941), 1, u'default'), u'Ir': ((0.0901961, 0.329412, 0.529412), 1, u'default'), u'Am': ((0.329412, 0.360784, 0.94902), 1, u'default'), u'Al': ((0.74902, 0.65098, 0.65098), 1, u'default'),
u'As': ((0.741176, 0.501961, 0.890196), 1, u'default'), u'Ar': ((0.501961, 0.819608, 0.890196), 1, u'default'), u'Au': ((1, 0.819608, 0.137255), 1, u'default'), u'At': ((0.458824, 0.309804, 0.270588), 1, u'default'), u'In': ((0.65098, 0.458824, 0.45098), 1, u'default')}
	materials = {u'default': ((0.85, 0.85, 0.85), 30)}
	pbInfo = {'category': [u'distance monitor', u'hydrogen bonds'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'labelOffset': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}, {'color': (8, 9, {}), 'atoms': [[16, 25], [11, 18], [59, 81], [62, 78], [90, 99], [85, 92], [127, 136], [122, 129]], 'label': (8, u'', {}), 'halfbond': (8, False, {}), 'labelColor': (8, None, {}), 'labelOffset': (8, chimera.Vector(-1e+99, 0.0, 0.0), {chimera.Vector(-1e+99, 0.0, 0.0): [0], chimera.Vector(-1e+99, 0.0, 0.0): [7], chimera.Vector(-1e+99, 0.0, 0.0): [6], chimera.Vector(-1e+99, 0.0, 0.0): [5], chimera.Vector(-1e+99, 0.0, 0.0): [4], chimera.Vector(-1e+99, 0.0, 0.0): [3], chimera.Vector(-1e+99, 0.0, 0.0): [2]}), 'drawMode': (8, 0, {}), 'display': (8, 2, {})}], 'lineType': (2, 1, {2: [0]}), 'color': (2, 8, {7: [0]}), 'optional': {'fixedLabels': (True, False, (2, False, {None: [1]}))}, 'display': (2, True, {}), 'showStubBonds': (2, False, {}), 'lineWidth': (2, 2.5, {1: [0]}),
'stickScale': (2, 1, {}), 'id': [-2, -1]}
	modelAssociations = {}
	colorInfo = (12, (u'', (0, 0, 1, 1)), {(u'H', (1, 1, 1, 1)): [5], (u'green', (0, 1, 0, 1)): [11], (u'N', (0.188235, 0.313725, 0.972549, 1)): [6], (u'', (1, 1, 1, 1)): [10], (u'O', (1, 0.0509804, 0.0509804, 1)): [4], (u'sky blue', (0.529412, 0.807843, 0.921569, 1)): [1], (u'tan', (0.823529, 0.705882, 0.54902, 1)): [0], (u'plum', (0.866667, 0.627451, 0.866667, 1)): [2], (u'light green', (0.564706, 0.933333, 0.564706, 1)): [3], (u'gray', (0.745, 0.745, 0.745, 1)): [8]})
	viewerInfo = {'cameraAttrs': {'center': (0.13691962280522, -4.1584880998617, 0.13299999046326), 'fieldOfView': 26.815645329743, 'nearFar': (11.208715212975, -10.942715232049), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 0.13299999046326}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': False, 'showShadows': False, 'viewSize': 14.715380383668, 'labelsOnTop': True, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 2, 'singleLayerTransparency': True, 'shadowTextureSize': 2048, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [(None, [(0.941176, 0.941176, 0.941176, 1), (0.741176, 0.741176, 0.741176, 1), (0.388235, 0.388235, 0.388235, 1)], 1), 1, 0, 0], 'depthCue': True, 'highlight': 0, 'scaleFactor': 1.3419417698829, 'angleDependentTransparency': True, 'backgroundMethod': 0}, 'viewerHL': 11, 'cameraMode': 'mono', 'detail': 1.5, 'viewerFog': None, 'viewerBG': 10}

	replyobj.status("Initializing session restore...", blankAfter=0,
		secondary=True)
	from SimpleSession.versions.v65 import expandSummary
	init(dict(enumerate(expandSummary(colorInfo))))
	replyobj.status("Restoring colors...", blankAfter=0,
		secondary=True)
	restoreColors(colors, materials)
	replyobj.status("Restoring molecules...", blankAfter=0,
		secondary=True)
	restoreMolecules(molInfo, resInfo, atomInfo, bondInfo, crdInfo)
	replyobj.status("Restoring surfaces...", blankAfter=0,
		secondary=True)
	restoreSurfaces(surfInfo)
	replyobj.status("Restoring VRML models...", blankAfter=0,
		secondary=True)
	restoreVRML(vrmlInfo)
	replyobj.status("Restoring pseudobond groups...", blankAfter=0,
		secondary=True)
	restorePseudoBondGroups(pbInfo)
	replyobj.status("Restoring model associations...", blankAfter=0,
		secondary=True)
	restoreModelAssociations(modelAssociations)
	replyobj.status("Restoring camera...", blankAfter=0,
		secondary=True)
	restoreViewer(viewerInfo)

try:
	restoreCoreModels()
except:
	reportRestoreError("Error restoring core models")

	replyobj.status("Restoring extension info...", blankAfter=0,
		secondary=True)


try:
	import StructMeasure
	from StructMeasure.DistMonitor import restoreDistances
	registerAfterModelsCB(restoreDistances, 1)
except:
	reportRestoreError("Error restoring distances in session")


def restoreMidasBase():
	formattedPositions = {}
	import Midas
	Midas.restoreMidasBase(formattedPositions)
try:
	restoreMidasBase()
except:
	reportRestoreError('Error restoring Midas base state')


def restoreMidasText():
	from Midas import midas_text
	midas_text.aliases = {'mmatch': 'hbonds intermodel false relax true angleSlop 40.0 color Blue linewidth 1.5; tile # spacingfactor 0.85 columns 2; color byhet;color red #0.1@O; color blue #0.2@O; color red #0.3@O; color red #0.4@O; color blue #0.5@O; color green #0.6@O', 'mylabel': 'labelopt info molecule; label offset 0,0.5,0 @/serialNumber=1; color black,al', 'simple': 'preset apply pub 1; light mode ambient; rep bs; set silhouette_width 3; setattr m stickScale .5; bondcolor black; color gray C', 'mytile': 'tile # spacingfactor $1 columns $2; color byhet', 'overlay': 'match #0.5 #0.3; match #0.6 #0.4; center; focus; preset apply pub 1', 'simpleWater': 'preset apply pub 1; light mode ambient; rep bs; set silhouette_width 3; setattr m stickScale .5; bondcolor gray; color red O; color white H', 'simpleB': 'preset apply pub 1; light mode ambient; rep bs; set silhouette_width 3; setattr m stickScale .5', 'pub1': 'preset apply pub 1', 'myhbonds': 'hbonds intermodel false relax true angleSlop 40.0 color Blue linewidth 2.5', 'MunkMatch': 'hbonds intermodel false ;tile # columns 2; match #0 #2  ; match #1 #3; center; focus; preset apply pub 1;color byhet', 'arrange': 'tile; center; focus'}
	midas_text.userSurfCategories = {}

try:
	restoreMidasText()
except:
	reportRestoreError('Error restoring Midas text state')


def restore_cap_attributes():
 cap_attributes = \
  {
   'cap_attributes': [ ],
   'cap_color': None,
   'cap_offset': 0.01,
   'class': 'Caps_State',
   'default_cap_offset': 0.01,
   'mesh_style': False,
   'shown': True,
   'subdivision_factor': 1.0,
   'version': 1,
  }
 import SurfaceCap.session
 SurfaceCap.session.restore_cap_attributes(cap_attributes)
registerAfterModelsCB(restore_cap_attributes)


def restore_volume_data():
 volume_data_state = \
  {
   'class': 'Volume_Manager_State',
   'data_and_regions_state': [ ],
   'version': 2,
  }
 from VolumeViewer import session
 session.restore_volume_data_state(volume_data_state)

try:
  restore_volume_data()
except:
  reportRestoreError('Error restoring volume data')

geomData = {'AxisManager': {}, 'CentroidManager': {}, 'PlaneManager': {}}

try:
	from StructMeasure.Geometry import geomManager
	geomManager._restoreSession(geomData)
except:
	reportRestoreError("Error restoring geometry objects in session")


def restoreSession_RibbonStyleEditor():
	import SimpleSession
	import RibbonStyleEditor
	userScalings = [('licorice', [[0.35, 0.35], [0.35, 0.35], [0.35, 0.35], [0.35, 0.35, 0.35, 0.35], [0.35, 0.35]])]
	userXSections = []
	userResidueClasses = []
	residueData = [(4, 'Chimera default', 'rounded', u'unknown'), (5, 'Chimera default', 'rounded', u'unknown'), (6, 'Chimera default', 'rounded', u'unknown'), (7, 'Chimera default', 'rounded', u'unknown')]
	flags = RibbonStyleEditor.NucleicDefault1
	SimpleSession.registerAfterModelsCB(RibbonStyleEditor.restoreState,
				(userScalings, userXSections,
				userResidueClasses, residueData, flags))
try:
	restoreSession_RibbonStyleEditor()
except:
	reportRestoreError("Error restoring RibbonStyleEditor state")

trPickle = 'gAJjQW5pbWF0ZS5UcmFuc2l0aW9ucwpUcmFuc2l0aW9ucwpxASmBcQJ9cQMoVQxjdXN0b21fc2NlbmVxBGNBbmltYXRlLlRyYW5zaXRpb24KVHJhbnNpdGlvbgpxBSmBcQZ9cQcoVQZmcmFtZXNxCEsBVQ1kaXNjcmV0ZUZyYW1lcQlLAVUKcHJvcGVydGllc3EKXXELVQNhbGxxDGFVBG5hbWVxDWgEVQRtb2RlcQ5VBmxpbmVhcnEPdWJVCGtleWZyYW1lcRBoBSmBcRF9cRIoaAhLFGgJSwFoCl1xE2gMYWgNaBBoDmgPdWJVBXNjZW5lcRRoBSmBcRV9cRYoaAhLAWgJSwFoCl1xF2gMYWgNaBRoDmgPdWJ1Yi4='
scPickle = 'gAJjQW5pbWF0ZS5TY2VuZXMKU2NlbmVzCnEBKYFxAn1xA1UHbWFwX2lkc3EEfXNiLg=='
kfPickle = 'gAJjQW5pbWF0ZS5LZXlmcmFtZXMKS2V5ZnJhbWVzCnEBKYFxAn1xA1UHZW50cmllc3EEXXEFc2Iu'
def restoreAnimation():
	'A method to unpickle and restore animation objects'
	# Scenes must be unpickled after restoring transitions, because each
	# scene links to a 'scene' transition. Likewise, keyframes must be 
	# unpickled after restoring scenes, because each keyframe links to a scene.
	# The unpickle process is left to the restore* functions, it's 
	# important that it doesn't happen prior to calling those functions.
	import SimpleSession
	from Animate.Session import restoreTransitions
	from Animate.Session import restoreScenes
	from Animate.Session import restoreKeyframes
	SimpleSession.registerAfterModelsCB(restoreTransitions, trPickle)
	SimpleSession.registerAfterModelsCB(restoreScenes, scPickle)
	SimpleSession.registerAfterModelsCB(restoreKeyframes, kfPickle)
try:
	restoreAnimation()
except:
	reportRestoreError('Error in Animate.Session')

def restoreLightController():
	import Lighting
	Lighting._setFromParams({'ratio': 1.25, 'brightness': 1.16, 'material': [30.0, (0.85, 0.85, 0.85), 1.0], 'back': [(0.35740674433659325, 0.6604015517481454, -0.6604015517481455), (1.0, 1.0, 1.0), 0.0], 'mode': 'two-point', 'key': [(-0.35740674433659325, 0.6604015517481454, 0.6604015517481455), (1.0, 1.0, 1.0), 1.0], 'contrast': 0.83, 'fill': [(0.25056280708573153, 0.25056280708573153, 0.9351131265310293), (1.0, 1.0, 1.0), 0.0]})
try:
	restoreLightController()
except:
	reportRestoreError("Error restoring lighting parameters")


try:
	import Ilabel
	il = Ilabel.LabelsModel(create=False)
	if il:
		il.destroy()
	il = Ilabel.LabelsModel()
	il.restoreSession({'labelIDs': ['label2d_id_1', 'label2d_id_2'], 'curLabel': 1, 'labels': [{'opacity': 1.0, 'lines': [[{'args': (u'I',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'n',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'i',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u't',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'i',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'a',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'l',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u' ',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'R',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'M',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'S',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'D',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u' ',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'=',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u' ',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'3',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'.',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'4',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'5',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'1',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}]], 'shown': True, 'args': ((0.415211970074813, 0.4943977591036415),), 'kw': {'margin': 9.0, 'outline': 0.0, 'background': None}}, {'opacity': 1.0, 'lines': [[{'args': (u'F',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'i',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'n',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'a',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'l',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u' ',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'R',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'M',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'S',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'D',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u' ',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'=',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u' ',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'0',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'.',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'7',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'4',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}, {'args': (u'6',), 'kw': {'baselineOffset': 0, 'fontName': 'Sans Serif', 'style': 0, 'rgba': (0, 0, 0, 1.0), 'size': 24}}]], 'shown': True, 'args': ((0.4177057356608478, 0.023809523809523808),), 'kw': {'margin': 9.0, 'outline': 0.0, 'background': None}}], 'labelUID': 3})
	del Ilabel, il
except:
	reportRestoreError("Error restoring IlabelModel instance in session")


try:
	from Ilabel.Arrows import ArrowsModel
	ArrowsModel().restore({'arrows': []})
except:
	reportRestoreError("Error restoring 2D arrows in session")



try:
	from Ilabel.ColorKey import getKeyModel
	getKeyModel()._restoreSession({'label spacing': 'proportional to value', 'label justification': 'decimal point', 'font size': 24, 'label positions': 'right/bottom', 'show ticks': False, 'border width': 2, 'label offset': 0, 'color depiction': 'blended', 'label color': (0, 0, 0), 'font name': 'Sans Serif', 'tick length': 10, 'border color': (0, 0, 0, 1.0), 'key position': None, 'font typeface': 0, 'tick thickness': 4, 'colors/labels': [((0, 0, 1, 1), 'min'), ((1, 1, 1, 1), ''), ((1, 0, 0, 1), 'max')]})
except:
	reportRestoreError("Error restoring color key")



def restore2DLabelDialog(info):
	from chimera.dialogs import find
	from Ilabel.gui import IlabelDialog
	dlg = find(IlabelDialog.name)
	if dlg is not None:
		dlg.destroy()
	dlg = find(IlabelDialog.name, create=True)
	dlg._restoreSession(info)

import SimpleSession
SimpleSession.registerAfterModelsCB(restore2DLabelDialog, {'mouse func': 'labeling', 'sel ranges': (), 'dialog shown': 1})



def restoreRemainder():
	from SimpleSession.versions.v65 import restoreWindowSize, \
	     restoreOpenStates, restoreSelections, restoreFontInfo, \
	     restoreOpenModelsAttrs, restoreModelClip, restoreSilhouettes

	curSelIds =  []
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 2 }
	windowSize = (802, 714)
	xformMap = {0: (((0.99523753752757, 0.040075980870349, -0.088860337909157), 40.082552528886), (-0.03372279673928, 0.21269912923873, -0.28176875690513), True), 1: (((0.13799258029922, -0.018409902720848, -0.99026214875869), 145.56395132774), (-0.013721227787983, -0.028761371437834, -0.32503712807485), True), 2: (((0.99523753752757, 0.040075980870349, -0.088860337909157), 40.082552528886), (-0.03372279673928, -9.4040298497287, -0.28176875690513), True), 3: (((0.93757134387581, 0.27230899073752, -0.21635107743298), 26.542012365524), (-0.084413500261519, -9.4087679162835, -0.22226206105264), True)}
	fontInfo = {'face': (u'Sans Serif', 'Bold', 12)}
	clipPlaneInfo = {}
	silhouettes = {0: True, 1: True, 2: True, 3: True, 312: True, 313: True}

	replyobj.status("Restoring window...", blankAfter=0,
		secondary=True)
	restoreWindowSize(windowSize)
	replyobj.status("Restoring open states...", blankAfter=0,
		secondary=True)
	restoreOpenStates(xformMap)
	replyobj.status("Restoring font info...", blankAfter=0,
		secondary=True)
	restoreFontInfo(fontInfo)
	replyobj.status("Restoring selections...", blankAfter=0,
		secondary=True)
	restoreSelections(curSelIds, savedSels)
	replyobj.status("Restoring openModel attributes...", blankAfter=0,
		secondary=True)
	restoreOpenModelsAttrs(openModelsAttrs)
	replyobj.status("Restoring model clipping...", blankAfter=0,
		secondary=True)
	restoreModelClip(clipPlaneInfo)
	replyobj.status("Restoring per-model silhouettes...", blankAfter=0,
		secondary=True)
	restoreSilhouettes(silhouettes)

	replyobj.status("Restoring remaining extension info...", blankAfter=0,
		secondary=True)
try:
	restoreRemainder()
except:
	reportRestoreError("Error restoring post-model state")
from SimpleSession.versions.v65 import makeAfterModelsCBs
makeAfterModelsCBs()

from SimpleSession.versions.v65 import endRestore
replyobj.status('Finishing restore...', blankAfter=0, secondary=True)
endRestore({})
replyobj.status('', secondary=True)
replyobj.status('Restore finished.')

