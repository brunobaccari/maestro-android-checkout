# Android checkout com Maestro

[English version](README.en.md)

Cinco fluxos no [My Demo App Android 2.3.0](https://github.com/saucelabs/my-demo-app-android/releases/tag/2.3.0), aplicativo público da Sauce Labs. O APK é baixado da release oficial; não há aplicação criada neste repositório.

## Executar

Instale Java 21, [Maestro CLI 2.11.0](https://docs.maestro.dev/maestro-cli/how-to-install-maestro-cli) e Android SDK. Inicie um emulador Android 34 com idioma inglês. No Windows, siga a configuração WSL da documentação do CLI.

```bash
cp .env.example .env
python -m pip install -r requirements.txt
python -c "from dotenv import load_dotenv; import os, urllib.request; load_dotenv(); urllib.request.urlretrieve(os.environ['APP_URL'], 'app.apk')"
adb install app.apk
python run_tests.py
```

O runner carrega `.env`; variáveis do processo têm prioridade. O Maestro recebe as variáveis `MAESTRO_*` pelo ambiente, sem credenciais nos YAMLs. Os usuários do exemplo são contas públicas do app. Os dados de endereço e cartão são fictícios e exclusivos desta demonstração.

## Cobertura

| Fluxo | Verificação |
| --- | --- |
| Checkout | Produto, subtotal de US$ 29,99, total com entrega de US$ 35,98, confirmação e carrinho vazio. |
| Quantidade | Dois itens somam US$ 59,98; reduzir retorna a US$ 29,99; retomar o app preserva dois itens e US$ 59,98. |
| Remoção | Excluir o último item mostra o estado vazio. |
| Usuário bloqueado | Mensagem de bloqueio e ausência do formulário de entrega. |
| Endereço obrigatório | Formulário vazio não abre pagamento e informa o nome ausente. |

Cada fluxo encerra o app antes de limpar seu estado. `flows/helpers/` reúne carrinho e login usados por mais de um cenário. Seletores usam IDs e descrições de acessibilidade do código público da versão fixada, sem coordenadas ou sleeps.

## QA e evidências

[Estratégia e exploração manual](docs/test-strategy.md), [casos para Xray](docs/xray-tests.csv), [exemplo de defeito em inglês](docs/defect-example.md) e [Execuções e artifacts no Actions](https://github.com/brunobaccari/maestro-android-checkout/actions).

O GitHub Actions instala o APK em emulador Android 34. Abra a execução em **Actions**: o **Summary** mostra contagens e status; em **Artifacts**, baixe `android-results` com JUnit, logs dos fluxos, screenshots disponíveis e uma cópia do resumo. Retenção: sete dias, inclusive quando um teste falha. Relatório ausente é informado como execução não confirmada, nunca como aprovação.

Falhas não são repetidas automaticamente. Não há cobertura iOS, dispositivo físico, compra real ou validação do backend comercial. O app de demonstração simula a compra.

Referências: [app e código oficial](https://github.com/saucelabs/my-demo-app-android/tree/2.3.0), [parâmetros Maestro](https://docs.maestro.dev/maestro-flows/flow-control-and-logic/parameters-and-constants), [emulador no CI](https://github.com/ReactiveCircus/android-emulator-runner).

## Critério de bloqueio e triagem

Total incorreto, conta bloqueada avançando, compra sem dados obrigatórios e carrinho inconsistente bloqueiam a execução. O cenário de quantidade também envia o app ao background e o retoma sem encerrar o processo; produto, quantidade e total precisam permanecer. Isso não cobre morte do processo, rotação ou dispositivo físico.

Todos os fluxos devem passar na versão fixada do APK, com JUnit e logs disponíveis no artifact. Ao falhar, separe instalação/boot/ADB de comportamento do app; compare screenshot, log do fluxo e seletor com o código dessa release antes de mudar uma expectativa. Uma falha intermitente permanece falha até investigação; não há retry automático de fluxo.

Datas de commits deste portfólio foram reorganizadas retroativamente; as execuções do Actions mantêm suas datas reais.

O summary do Actions lista cada cenário, duração, totais e motivo de bloqueio. O gate exige a quantidade prevista no workflow, sem falhas ou skips; JUnit ausente ou inválido reprova. O resumo também acompanha o artifact.

Husky: com Node 24 e as dependências da stack instalados, rode `npm ci` para ativar o pre-commit. `npm run check:local` verifica o diff, o gate dos relatórios e os checks de tipos/lint existentes. O hook também bloqueia arquivos ignorados no índice. Testes que usam navegador, emulador ou API continuam no CI.
