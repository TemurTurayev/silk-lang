import * as path from "path";
import * as vscode from "vscode";
import {
  LanguageClient,
  LanguageClientOptions,
  ServerOptions,
  TransportKind,
} from "vscode-languageclient/node";

let client: LanguageClient | undefined;

export function activate(context: vscode.ExtensionContext): void {
  const config = vscode.workspace.getConfiguration("silk.lsp");
  const enabled = config.get<boolean>("enabled", true);

  if (!enabled) {
    return;
  }

  const serverCommand = resolveServerCommand(config);

  if (!serverCommand) {
    vscode.window.showWarningMessage(
      "Silk LSP: Could not find 'silk-lsp' command. " +
        "Install with: pip install silk-lang[lsp]"
    );
    return;
  }

  const serverOptions: ServerOptions = {
    command: serverCommand,
    args: ["--stdio"],
    transport: TransportKind.stdio,
  };

  const clientOptions: LanguageClientOptions = {
    documentSelector: [{ scheme: "file", language: "silk" }],
    synchronize: {
      fileEvents: vscode.workspace.createFileSystemWatcher("**/*.silk"),
    },
  };

  client = new LanguageClient(
    "silk-language-server",
    "Silk Language Server",
    serverOptions,
    clientOptions
  );

  client.start();
  context.subscriptions.push({
    dispose: () => {
      if (client) {
        client.stop();
      }
    },
  });
}

export function deactivate(): Thenable<void> | undefined {
  if (client) {
    return client.stop();
  }
  return undefined;
}

function resolveServerCommand(
  config: vscode.WorkspaceConfiguration
): string | undefined {
  const custom = config.get<string>("serverCommand", "");
  if (custom) {
    return custom;
  }

  // Try common locations
  const candidates = [
    "silk-lsp",
    "python3 -m silk.lsp",
    "python -m silk.lsp",
  ];

  // For now, return the default command name.
  // The language client will handle if it's not found.
  return "silk-lsp";
}
